# FlytBase Internship – Full-Stack Demo

## Overview
This project is a full-stack demo built using **React (Vite)** and **FastAPI**.
It demonstrates frontend–backend integration, clean API design, async handling,
environment-based configuration, and production-style project structure.

The app accepts a user's name and age and returns a computed response via a backend API.

---

## Tech Stack
- Frontend: React + Vite
- Backend: FastAPI + Pydantic
- Tooling: npm, uvicorn, Python venv
- API Communication: REST (JSON)

---

## Project Structure
flytbase-fullstack-demo/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI app entry
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   └── predict.py       # /predict endpoint
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   └── predict.py       # Pydantic models
│   │   └── services/
│   │       ├── __init__.py
│   │       └── model_service.py # ML / logic layer
│   │
│   ├── requirements.txt         # Python dependencies
│   ├── .env.example             # Sample env vars
│   └── README.md                # Backend instructions
│
├── frontend/
│   ├── public/
│   │   └── index.html
│   │
│   ├── src/
│   │   ├── api/
│   │   │   └── predictApi.js    # Axios API call
│   │   │
│   │   ├── components/
│   │   │   ├── Predictor.jsx
│   │   │   └── Loader.jsx
│   │   │
│   │   ├── pages/
│   │   │   └── Home.jsx
│   │   │
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   │
│   ├── .env.example             # VITE_API_URL
│   ├── package.json
│   ├── vite.config.js
│   └── README.md                # Frontend instructions
│
├── .gitignore                   # VERY IMPORTANT
├── README.md                    # Root project README
└── LICENSE (optional)
