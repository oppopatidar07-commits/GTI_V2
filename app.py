
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "status": "GTI Server Running",
        "api_key_found": bool(os.getenv("API_KEY")),
        "client_code_found": bool(os.getenv("CLIENT_CODE")),
        "pin_found": bool(os.getenv("PIN")),
        "totp_secret_found": bool(os.getenv("TOTP_SECRET"))
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
