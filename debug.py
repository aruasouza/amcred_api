from flask import Flask
from routes import main as main_blueprint

def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    app.register_blueprint(main_blueprint)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug = True)