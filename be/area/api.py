from fastapi import APIRouter, Body, Request, Form, Response, HTTPException, status
import uuid, json
from fastapi.encoders import jsonable_encoder
from typing import List

from be.area.model import areaCreate,areaUpdate

area_api = APIRouter()

#create
@area_api.post("/", response_description="Create a new area", status_code=status.HTTP_201_CREATED, response_model=areaCreate)
async def create_area(request: Request, p_area: areaCreate = Body(...)):
    j_area = jsonable_encoder(p_area)
    new_area = request.app.database["areas"].insert_one(j_area)
    
    created_area = request.app.database["areas"].find_one(
        {"_id": new_area.inserted_id}
    )
    return created_area


# list    
@area_api.get("/", response_description="List all areas")
def list_area(request: Request):
    areas = list(request.app.database["areas"].find({}))
    return areas

#delete
@area_api.delete("/{id}", response_description="Delete a area")
def delete_area(id: str, request: Request, response: Response):
    delete_result = request.app.database["areas"].delete_one({"_id": id})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Author not found")
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)


#find
@area_api.get("/{id}", response_description="Get a single area by id")
def find_area(id: str, request: Request):
    area = request.app.database["areas"].find_one({"_id": id})
    return area   
    
#UPDATE 
@area_api.post("/{id}", response_description="Update a area", response_model=areaUpdate)
async def update_area(id: str, request: Request, area: areaUpdate = Body(...)):
    j_area = jsonable_encoder(area)
    update_result = request.app.database["areas"].update_one(
        {"_id": id}, {"$set": j_area}
    )
    updated_area = request.app.database["areas"].find_one({"_id": id})    
    return updated_area
 