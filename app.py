from flask import Flask, jsonify

from constants import PROJECT_NAME
from strategy import get_signal
from market_data import get_market_status
from utils import current_date, current_time

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
    "project": PROJECT_NAME,
    "status": "Running",
    "date": current_date(),
    "time": current_time(),
    "market": get_market_status(),
    "signal": get_signal()
})


@app.route("/health")
def health():
    return jsonify({
        "status": "OK"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
