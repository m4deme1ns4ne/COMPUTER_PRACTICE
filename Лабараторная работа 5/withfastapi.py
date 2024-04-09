from fastapi import FastAPI
from fastapi.responses import JSONResponse
import datetime


app = FastAPI()

@app.get("/")
def get_name():
    current_time = datetime.datetime.now().strftime("%d.%m.%y %H:%M:%S")
    content = {"name": "Волжанин Александр", "datetime": current_time}
    headers = {"Content-Type": "application/json; charset=utf-8"}
    return JSONResponse(content=content, headers=headers)
