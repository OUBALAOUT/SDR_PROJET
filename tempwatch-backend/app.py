from flask import Flask,Blueprint,render_template, request, jsonify
from db_config import get_db, close_db
from flask_cors import CORS

app = Flask(__name__, template_folder='../public/templates', static_folder='../public/static')
CORS(app)

# Importation des blueprints
from routes.auth import auth_bp
from routes.capteurs import capteur_bp
from routes.donnees import donnees_bp
from routes.alertes import alerte_bp
from routes.utilisateurs import user_bp

# Enregistrement des routes
app.register_blueprint(auth_bp)
app.register_blueprint(capteur_bp)
app.register_blueprint(donnees_bp)
app.register_blueprint(alerte_bp)
app.register_blueprint(user_bp)

@app.teardown_appcontext
def teardown(exception):
    close_db()
# ...existing code...

@app.route('/acceuil')
def index():
    return render_template('acceuil.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/logout')
def logout():
    return render_template('logout.html')
@app.route('/tableboard')
def tableboard():
    return render_template('tableboard.html')
@app.route('/profile')
def profile():
    return render_template('profile.html')
@app.route('/alerte')
def alerte():
    return render_template('alerte.html')
@app.route('/capteur')
def capteur():
    return render_template('capteur.html')
@app.route('/parametres')
def parametres():
    return render_template('parametres.html')
@app.route('/help')
def help():
    return render_template('help.html')

#def index():
 #   return send_from_directory('Public', 'index.html')
if __name__ == '__main__':
    app.run(debug=True)
