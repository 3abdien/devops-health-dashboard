import os
import sqlite3
import json
from flask import Flask, render_template, jsonify

# Setup
app = Flask(__name__, template_folder="templates")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH  = os.path.join(BASE_DIR, "data", "metrics.db")

def get_metrics():
    """Fetch last 20 metrics from database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT timestamp, cpu_pct, mem_pct, disk_pct
        FROM metrics
        ORDER BY id DESC
        LIMIT 20
    """)
    rows = cursor.fetchall()
    conn.close()
    # Reverse so oldest is first on the chart
    rows.reverse()
    return rows

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/metrics")
def api_metrics():
    """JSON endpoint that Chart.js will call."""
    rows = get_metrics()
    data = {
        "labels":  [row[0] for row in rows],
        "cpu":     [row[1] for row in rows],
        "memory":  [row[2] for row in rows],
        "disk":    [row[3] for row in rows],
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)