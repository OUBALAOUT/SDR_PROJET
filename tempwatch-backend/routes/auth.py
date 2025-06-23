from flask import Blueprint, request, jsonify
from db_config import get_db
import bcrypt

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    mot_de_passe = data['password']

    db = get_db()
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM utilisateur WHERE email = %s", (email,))
        user = cursor.fetchone()

    if user and bcrypt.checkpw(mot_de_passe.encode(), user['mot_de_passe'].encode()):
        return jsonify({'message': 'Connexion réussie', 'user': user})
    else:
        return 1
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    nom = data['name']
    email = data['email']
    mot_de_passe = data['password']

    hashed_pw = bcrypt.hashpw(mot_de_passe.encode(), bcrypt.gensalt()).decode()

    db = get_db()
    try:
        with db.cursor() as cursor:
            cursor.execute("INSERT INTO utilisateur (nom, email, mot_de_passe) VALUES (%s, %s, %s)",
                           (nom, email, hashed_pw))
        db.commit()
        return jsonify({'message': 'Utilisateur enregistré avec succès'}), 201
    except Exception as e:
        db.rollback()
        return jsonify({'message': 'Erreur : ' + str(e)}), 500