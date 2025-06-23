from flask import Blueprint, request, jsonify
from db_config import get_db

capteur_bp = Blueprint('capteur', __name__, url_prefix='/capteurs')

@capteur_bp.route('/', methods=['GET'])
def get_capteurs():
    db = get_db()
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM capteur")
        result = cursor.fetchall()
    return jsonify(result)

@capteur_bp.route('/', methods=['POST'])
def ajouter_capteur():
    data = request.json
    db = get_db()
    with db.cursor() as cursor:
        cursor.execute("""
            INSERT INTO capteur (nom_capteur, localisation, type_capteur, date_installation)
            VALUES (%s, %s, %s, NOW())
        """, (data['nom_capteur'], data['localisation'], data['type_capteur']))
        db.commit()
    return jsonify({'message': 'Capteur ajouté'})
