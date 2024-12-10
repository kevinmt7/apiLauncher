from flask import Flask, jsonify
import os

app = Flask(__name__)

# Datos de los juegos (esto puede ser reemplazado por una base de datos en el futuro)
games = [
    {
        "name": "Juego 1",
        "cover": "https://example.com/caratula1.jpg",
        "url": "https://example.com/juego1.rar",
        "description": "Este es un juego emocionante lleno de aventuras y retos."
    },
    {
        "name": "Juego 2",
        "cover": "https://example.com/caratula2.jpg",
        "url": "https://example.com/juego2.rar",
        "description": "Un juego de estrategia para desafiar tu mente."
    },
    {
        "name": "Juego 3",
        "cover": "https://example.com/caratula3.jpg",
        "url": "https://example.com/juego3.rar",
        "description": "Explora un mundo abierto lleno de posibilidades."
    }
]

@app.route('/games', methods=['GET'])
def get_games():
    return jsonify(games)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
