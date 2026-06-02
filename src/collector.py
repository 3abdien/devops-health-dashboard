import psutil
import sqlite3
import datetime
import os

# --- Database Setup ---
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'metrics.db')

def init_db():
    """Create the metrics table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS metrics (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            cpu_pct   REAL NOT NULL,
            mem_pct   REAL NOT NULL,
            disk_pct  REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("✅ Database initialized.")

# --- Metric Collection ---
def collect_metrics():
    """Collect current system metrics and save to DB."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu     = psutil.cpu_percent(interval=1)
    memory  = psutil.virtual_memory().percent
    disk    = psutil.disk_usage('/').percent

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO metrics (timestamp, cpu_pct, mem_pct, disk_pct)
        VALUES (?, ?, ?, ?)
    ''', (timestamp, cpu, memory, disk))
    conn.commit()
    conn.close()

    print(f"[{timestamp}] CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")

# --- Entry Point ---
if __name__ == "__main__":
    init_db()
    print("📊 Collecting system metrics...")
    for i in range(5):
        collect_metrics()
    print("✅ Done. Check data/metrics.db")