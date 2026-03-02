# 🏎️ F1 Strategy Dashboard

![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?style=flat&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-18-61DAFB?style=flat&logo=react&logoColor=black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=flat&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=flat&logo=docker&logoColor=white)

A full-stack F1 race strategy dashboard built with FastAPI, React, PostgreSQL, and Docker — visualizing lap times, tire strategies, and pit stops using the FastF1 API.

---

## Features

- 📅 **Race Selector** — Browse any race from any F1 season
- 📈 **Lap Time Chart** — Compare lap time evolution across drivers throughout a race
- 🛞 **Tire Strategy View** — Visual timeline of each driver's tire stints and compounds
- 🔧 **Pit Stop Table** — Full pit stop breakdown with lap numbers per driver
- ⚡ **DB Caching** — Race data is fetched once from FastF1 and stored in PostgreSQL for instant repeat loads
- 🐳 **Fully Dockerized** — One command to spin up the entire stack

---

## Tech Stack

| Layer | Technology |
|---|---|
| Data Source | [FastF1](https://github.com/theOehrly/Fast-F1) Python API |
| Backend | FastAPI + SQLAlchemy |
| Database | PostgreSQL 15 |
| Frontend | React 18 + Recharts |
| Containerization | Docker + Docker Compose |

---

## Getting Started

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Node.js 18+](https://nodejs.org/)
- [Python 3.11+](https://www.python.org/)

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/f1-strategy-dashboard.git
cd f1-strategy-dashboard
```

### 2. Start the database
```bash
docker-compose up -d
```

### 3. Start the backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs at `http://localhost:8000`  
Interactive API docs at `http://localhost:8000/docs`

### 4. Start the frontend
```bash
cd frontend
npm install
npm start
```

Frontend runs at `http://localhost:3000`

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| GET | `/schedule/{year}` | Full race calendar for a season |
| GET | `/race/{year}/{round}/laps` | Lap times for all drivers in a race |
| GET | `/race/{year}/{round}/pitstops` | Pit stop data for a race |

---

## Project Structure
```
f1-strategy-dashboard/
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── RaceSelector.jsx
│   │   │   ├── LapTimeChart.jsx
│   │   │   ├── TireStrategy.jsx
│   │   │   └── PitStopTable.jsx
│   │   └── App.jsx
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## Future Improvements

- [ ] Driver telemetry comparison (speed, throttle, braking)
- [ ] Weather data overlay on lap time chart
- [ ] Mobile responsive layout
- [ ] Deploy to AWS / Render

---

## Acknowledgements

- [FastF1](https://github.com/theOehrly/Fast-F1) by theOehrly for the incredible F1 data API
