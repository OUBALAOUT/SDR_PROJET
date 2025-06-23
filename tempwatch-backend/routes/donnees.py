from flask import Blueprint, request, jsonify
from db_config import get_db

donnees_bp = Blueprint('donnees', __name__, url_prefix='/donnees')



# In routes/donnees.py

@donnees_bp.route('/api/max-temperature')
def api_max_temperature():
    db = get_db()
    with db.cursor() as cursor:
        # Use an alias 'max_temp' for the result of MAX(temperature)
        cursor.execute("SELECT MAX(temperature) AS max_temp FROM donnee_capteur")
        result = cursor.fetchone()  # This will return something like {'max_temp': 25.5}

        # Check if the result and the value associated with the 'max_temp' key are not None
        if result and result['max_temp'] is not None:
            max_temp = result['max_temp']
        else:
            max_temp = 0  # Default value if table is empty or temperature is NULL

    return jsonify({"temperature": max_temp})

@donnees_bp.route('/api/recent-temperatures')
def get_temperatures():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, capteur_id, temperature, date FROM donnee_capteur ORDER BY date DESC LIMIT 10")
    data = cursor.fetchall()
    cursor.close()
    return jsonify([{
        "id": row[0],
        "capteur_id": row[1],
        "temperature": row[2],
        "date": str(row[3])
    } for row in data])
    
@donnees_bp.route('/api/dashboard')
def dashboard_data():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        SELECT capteur_id, temperature, MAX(date) 
        FROM donnee_capteur 
        GROUP BY capteur_id
    """)
    results = cursor.fetchall()

    data = []
    for capteur_id, temperature, date in results:
        status = "Actif" if temperature is not None else "Inactif"
        data.append({
            "capteur_id": capteur_id,
            "temperature": temperature,
            "status": status,
            "last_update": str(date)
        })

    cursor.close()
    return jsonify(data)
@donnees_bp.route('/api/capteurs')
def api_capteurs():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        SELECT capteur_id, temperature 
        FROM donnee_capteur 
        WHERE (capteur_id, date_heure) IN (
            SELECT capteur_id, MAX(date_heure)
            FROM donnee_capteur
            GROUP BY capteur_id
        )
        ORDER BY capteur_id
    """)
    rows = cursor.fetchall()
    cursor.close()

    data = []
    for row in rows:
        data.append({
            "capteur_id": row[0],
            "temperature": row[1]
        })

    return jsonify(data)
