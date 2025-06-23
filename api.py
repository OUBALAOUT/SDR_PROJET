# flask_gateway.py
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def handle_temperature():
    data = request.json
    id = data['id']
    capteur_id = data['capteur_id']
    temperature = data['temperature']
    
    # Call your Java CORBA client with data
    subprocess.run([
        "java", "SensorClient", id, capteur_id, str(temperature)
    ])
    return "Data sent to CORBA", 200

app.run(host='127.0.0.1', port=5000)
