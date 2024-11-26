from fastapi import APIRouter, Body, Request, Form, Response, HTTPException, status
import uuid, json
from fastapi.encoders import jsonable_encoder
from typing import List

from be.center.model import centerCreate,centerUpdate

center_api = APIRouter()

#create
@center_api.post("/", response_description="Create a new center", status_code=status.HTTP_201_CREATED, response_model=centerCreate)
async def create_center(request: Request, p_center: centerCreate = Body(...)):
    j_center = jsonable_encoder(p_center)
    new_center = request.app.database["centers"].insert_one(j_center)
    
    created_center = request.app.database["centers"].find_one(
        {"_id": new_center.inserted_id}
    )
    return created_center


# list    
@center_api.get("/", response_description="List all centers")
def list_center(request: Request):
    centers = list(request.app.database["centers"].find({}))
    return centers

#delete
@center_api.delete("/{id}", response_description="Delete a center")
def delete_center(id: str, request: Request, response: Response):
    delete_result = request.app.database["centers"].delete_one({"_id": id})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Author not found")
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)


#find
@center_api.get("/{id}", response_description="Get a single center by id")
def find_center(id: str, request: Request):
    center = request.app.database["centers"].find_one({"_id": id})
    return center   
    
#UPDATE 
@center_api.post("/{id}", response_description="Update a center", response_model=centerUpdate)
async def update_center(id: str, request: Request, center: centerUpdate = Body(...)):
    j_center = jsonable_encoder(center)
    update_result = request.app.database["centers"].update_one(
        {"_id": id}, {"$set": j_center}
    )
    updated_center = request.app.database["centers"].find_one({"_id": id})    
    return updated_center
 