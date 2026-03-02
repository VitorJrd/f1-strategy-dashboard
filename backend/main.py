from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import fastf1
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

fastf1.Cache.enable_cache("cache")  

@app.get("/")
def root():
    return {"message": "F1 Dashboard API"}

@app.get("/race/{year}/{round}/laps")
def get_lap_times(year: int, round: int):
    session = fastf1.get_session(year, round, "R")
    session.load(telemetry=False, weather=False)
    laps = session.laps[["Driver", "LapNumber", "LapTime", "Compound"]].copy()
    laps["LapTime"] = laps["LapTime"].dt.total_seconds()
    laps = laps.dropna()
    return laps.to_dict(orient="records")

@app.get("/race/{year}/{round}/pitstops")
def get_pit_stops(year: int, round: int):
    session = fastf1.get_session(year, round, "R")
    session.load(telemetry=False, weather=False)
    laps = session.laps[["Driver", "LapNumber", "PitInTime", "Compound"]].dropna(subset=["PitInTime"])
    laps["PitInTime"] = laps["PitInTime"].dt.total_seconds()
    return laps.to_dict(orient="records")

@app.get("/schedule/{year}")
def get_schedule(year: int):
    schedule = fastf1.get_event_schedule(year)
    return schedule[["RoundNumber", "EventName", "Country"]].to_dict(orient="records")
