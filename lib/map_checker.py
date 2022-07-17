import requests
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

def mapCheck(mode: str) -> dict:
    if mode not in ["battle_royale", "arenas", "ranked", "arenasRanked", "control"]:
        return None

    YOUR_API_KEY = os.getenv("APEX_STUTE_API_KEY")

    r = requests.get(f"https://api.mozambiquehe.re/maprotation?auth={YOUR_API_KEY}&version=3")
    data = eval(r._content.decode("utf-8"))

    start_time = datetime.datetime.fromtimestamp(data[mode]["current"]["start"], tz=datetime.timezone(datetime.timedelta(hours=8))).time()
    end_time = datetime.datetime.fromtimestamp(data[mode]["current"]["end"], tz=datetime.timezone(datetime.timedelta(hours=8))).time()
    
    modeDict = {"battle_royale":"大逃殺", "arenas":"競技場", "ranked":"大逃殺(積分)", "arenasRanked":"競技場(積分)", "control":"控制"}

    return {"mode":modeDict[mode], "currentMap":data[mode]["current"]["map"], "startTime":f"{start_time.hour:0>2}:{start_time.minute:0>2}", "endTime":f"{end_time.hour:0>2}:{end_time.minute:0>2}", "nextMap":data[mode]["next"]["map"]}
