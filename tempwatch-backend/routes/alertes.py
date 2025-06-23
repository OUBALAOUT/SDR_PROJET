from flask import Blueprint, request, jsonify
from db_config import get_db

alerte_bp = Blueprint('alerte', __name__, url_prefix='/alertes')

@alerte_bp.route('/', methods=['GET'])
def get_alertes():
    db = get_db()
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM alerte ORDER BY date_alerte DESC")
        result = cursor.fetchall()
    return jsonify(result)

@alerte_bp.route('/', methods=['POST'])
def creer_alerte():
    data = request.json
    db = get_db()
    with db.cursor() as cursor:
        cursor.execute("""
            INSERT INTO alerte (capteur_id, utilisateur_id, type_alerte, message, date_alerte)
            VALUES (%s, %s, %s, %s, NOW())
        """, (
            data['capteur_id'],
            data['utilisateur_id'],
            data['type_alerte'],
            data['message']
        ))
        db.commit()
    return jsonify({'message': 'Alerte créée'})
