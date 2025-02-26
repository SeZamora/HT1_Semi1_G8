from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return "OK", 200
@app.route('/check', methods=['GET'])
def check():
    return "OK", 200

@app.route('/info', methods=['GET'])
def info():
    data = {
        "Instancia": "Maquina 1 - API 1",
        "Curso": "Seminario de Sistemas 1 A",
        "Grupo" : "Grupo 8"
    }
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
