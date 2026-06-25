from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def landing():
        return render_template('index.html')

    @app.route('/inicio')
    def inicio():
        return "Entré correctamente a /inicio"

    return app