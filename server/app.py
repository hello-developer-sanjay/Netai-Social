# app.py
from flask import Flask
from flask_cors import CORS
from routes.message_routes import message_routes

app = Flask(__name__)
app.register_blueprint(message_routes)

# Enable CORS for all routes
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
