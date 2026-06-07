import os
import sqlite3
from flask import Flask

# Setup
app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH  = os.path.join(BASE_DIR, "data", "metrics.db")

# Helper function to read metrics from database
def get_metrics():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT timestamp, cpu_pct, mem_pct, disk_pct
        FROM metrics
        ORDER BY id DESC
        LIMIT 10
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

# Home route
@app.route("/")
def home():
    metrics = get_metrics()

    # Build a simple HTML page
    html = """
    <html>
    <head>
        <title>DevOps Health Dashboard</title>
        <style>
            body  { font-family: Arial; padding: 30px; background: #0f172a; color: #e2e8f0; }
            h1    { color: #38bdf8; }
            table { border-collapse: collapse; width: 100%; margin-top: 20px; }
            th    { background: #1e293b; padding: 12px; text-align: left; color: #38bdf8; }
            td    { padding: 10px; border-bottom: 1px solid #1e293b; }
            tr:hover { background: #1e293b; }
            .ok       { color: #4ade80; }
            .warning  { color: #facc15; }
            .critical { color: #f87171; }
        </style>
    </head>
    <body>
        <h1>🖥️ DevOps Health Dashboard</h1>
        <p>Last 10 system metrics readings</p>
        <table>
            <tr>
                <th>Timestamp</th>
                <th>CPU %</th>
                <th>Memory %</th>
                <th>Disk %</th>
                <th>Status</th>
            </tr>
    """

    for row in metrics:
        timestamp, cpu, mem, disk = row

        # Determine status
        if cpu > 85 or mem > 85 or disk > 85:
            status = '<span class="critical">⚠️ CRITICAL</span>'
        elif cpu > 70 or mem > 70 or disk > 70:
            status = '<span class="warning">⚡ WARNING</span>'
        else:
            status = '<span class="ok">✅ OK</span>'

        html += f"""
            <tr>
                <td>{timestamp}</td>
                <td>{cpu}%</td>
                <td>{mem}%</td>
                <td>{disk}%</td>
                <td>{status}</td>
            </tr>
        """

    html += """
        </table>
    </body>
    </html>
    """
    return html

# Entry point
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

