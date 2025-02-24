from flask import Flask, jsonify
import logging

app = Flask(__name__)

# Configuração de logs
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(message)s")

@app.route("/")
def home():
    return "Aplicação Flask rodando!"

@app.route("/health")
def health():
    logging.info("Health check realizado.")
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)