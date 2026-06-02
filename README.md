# 🖥️ DevOps Health Dashboard

A lightweight system monitoring tool built with Python and SQLite.
Collects real-time CPU, memory, and disk metrics and stores them
in a local database — designed to demonstrate core DevOps observability principles.

![Python](https://img.shields.io/badge/Python-3.14-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📋 Features

- ✅ Real-time CPU, memory, and disk usage collection
- ✅ Persistent storage with SQLite
- ✅ Lightweight — no cloud dependency, runs anywhere
- ✅ Foundation for a full web dashboard (in progress)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.14 | Core scripting |
| psutil | System metrics collection |
| SQLite | Lightweight local database |
| Flask | Web dashboard (coming soon) |
| Docker | Containerization (coming soon) |
| GitHub Actions | CI/CD pipeline (coming soon) |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/ahmed abdien/devops-health-dashboard.git
cd devops-health-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the collector
python src/collector.py
```
# ✅ Database initialized.
# 📊 Collecting system metrics...
# [date ] CPU: 1.0% | Memory: 74.8% | Disk: 88.5%
# [date] CPU: 0.7% | Memory: 74.8% | Disk: 88.5%
# ✅ Done. Check data/metrics.db 
---

## 📁 Project Structure
devops-health-dashboard/
├── src/
│   ├── collector.py      # Metrics collection + SQLite storage
│   └── dashboard.py      # Web dashboard (in progress)
├── data/
│   └── metrics.db        # SQLite database (auto-generated)
├── requirements.txt      # Python dependencies
└── README.md
---

## 🗺️ Roadmap

- [x] System metrics collector
- [x] SQLite storage
- [ ] Flask web dashboard
- [ ] Docker containerization
- [ ] GitHub Actions CI/CD pipeline
- [ ] Deploy to cloud (AWS/GCP)

---

## 👤 Author

**<Your Full Name>**
- GitHub: [@<your-username>](https://github.com/<your-username>)
- LinkedIn: [<your-name>](https://linkedin.com/in/<your-linkedin>)

---

## 📄 License

This project is licensed under the MIT License.