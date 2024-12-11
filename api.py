from flask import Flask, jsonify
import os

app = Flask(__name__)

# Datos de los juegos (esto puede ser reemplazado por una base de datos en el futuro)
games = [
    {
        "name": "DOOM 64",
        "cover": "https://m.media-amazon.com/images/M/MV5BOGFjN2E1ZTQtZWQwZC00MWZjLTkwYWItZTNlYjBmNDY4MGJmXkEyXkFqcGc@._V1_.jpg",
        "url": "https://huggingface.co/spaces/Panisis/Why/resolve/main/DOOM%2064.7z",
        "description": "Este es un juego emocionante lleno de aventuras y retos."
    },
    {
        "name": "FNAF SAGA (1,2,3)",
        "cover": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/819855d5-f31e-4d21-8563-66db05a4e8f3/dfrq4la-1a00c730-e39b-488f-855c-fe7a6ce1be96.png/v1/fill/w_1280,h_1793,q_80,strp/_blender_3_4_fnaf1__fnaf_1_cover_art_by_springyt_dfrq4la-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTc5MyIsInBhdGgiOiJcL2ZcLzgxOTg1NWQ1LWYzMWUtNGQyMS04NTYzLTY2ZGIwNWE0ZThmM1wvZGZycTRsYS0xYTAwYzczMC1lMzliLTQ4OGYtODU1Yy1mZTdhNmNlMWJlOTYucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.1eNsOBnXqgEtQZ9zOovNKy3rDA3HIUc4ZxXls2JK05I",
        "url": "https://huggingface.co/spaces/Panisis/Why/resolve/main/Five%20Nights%20At%20Freddy's.7z",
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
