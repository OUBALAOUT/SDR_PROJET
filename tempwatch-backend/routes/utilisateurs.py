from flask import Blueprint, request, jsonify
from db_config import get_db
import bcrypt

user_bp = Blueprint('user', __name__, url_prefix='/utilisateurs')

@user_bp.route('/', methods=['GET'])
def get_utilisateurs():
    db = get_db()
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM utilisateur")
        result = cursor.fetchall()
    return jsonify(result)

@user_bp.route('/', methods=['POST'])
def ajouter_utilisateur():
    data = request.json
    hashed = bcrypt.hashpw(data['mot_de_passe'].encode(), bcrypt.gensalt())
    db = get_db()
    with db.cursor() as cursor:
        cursor.execute("""
            INSERT INTO utilisateur (nom, prenom, email, mot_de_passe, role)
            VALUES (%s, %s, %s, %s, %s)
        """, (data['nom'], data['prenom'], data['email'], hashed.decode(), data['role']))
        db.commit()
    return jsonify({'message': 'Utilisateur ajouté'})
