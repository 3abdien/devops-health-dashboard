import os
import datetime
import random
import string
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

print(f"Data folder is at: {DATA_DIR}")
# Write a simple file
report_path = os.path.join(DATA_DIR, "health_report.txt")

with open(report_path, "w") as f:
    f.write("=== Server Health Report ===\n")
    f.write("Web-Server-1 | CPU: 74.8% | Memory: 80% | OK\n")
    f.write("Web-Server-2 | CPU: 82.3% | Memory: 88.3% | WARNING\n")

print("Report saved!")
# Read the file back
with open(report_path, "r") as f:
    content = f.read()

print("--- Reading the file back ---")
print(content)