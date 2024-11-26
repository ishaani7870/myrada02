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
app.database = app.mongodb_client[config["DB_BOOK"]]

# from be.author.api import author_api as author_apiroutes
# app.include_router(author_apiroutes, tags=["authors"], prefix="/api/author")

# from be.book.api import book_api as book_apiroutes
# app.include_router(book_apiroutes, tags=["books"], prefix="/api/book")

# from be.member.api import member_api as member_apiroutes
# app.include_router(member_apiroutes, tags=["members"], prefix="/api/member")

@app.get("/")
async def home(request: Request):
  return FileResponse('fe/index.html')
  
  
