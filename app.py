from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "BIG WDC ENERGY. Visit /ping to test.", 200

@app.route("/ping")
def ping():
    return "200 OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
