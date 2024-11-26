import uvicorn
from fastapi import FastAPI, Request, Form
from dotenv import dotenv_values
from pymongo import MongoClient
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

config = dotenv_values(".env")
app = FastAPI()
app.mount("/fe", StaticFiles(directory="fe"),name="fe")

app.mongodb_client = MongoClient(config["CONNECTION_STRING"])
app.database = app.mongodb_client[config["DB_AREA"]]

from be.area.api import area_api as area_apiroutes
app.include_router(area_apiroutes, tags=["areas"], prefix="/api/area")

from be.center.api import center_api as center_apiroutes
app.include_router(center_apiroutes, tags=["centers"], prefix="/api/center")

# from be.member.api import member_api as member_apiroutes
# app.include_router(member_apiroutes, tags=["members"], prefix="/api/member")

@app.get("/")
async def home(request: Request):
  return FileResponse('fe/index.html')
  
  
