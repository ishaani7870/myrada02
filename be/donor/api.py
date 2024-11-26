from fastapi import APIRouter, Body, Request, Form, Response, HTTPException, status
import uuid, json
from fastapi.encoders import jsonable_encoder
from typing import List

from be.donor.model import donorCreate,donorUpdate

donor_api = APIRouter()

#create
@donor_api.post("/", response_description="Create a new donor", status_code=status.HTTP_201_CREATED, response_model=donorCreate)
async def create_donor(request: Request, p_donor: donorCreate = Body(...)):
    j_donor = jsonable_encoder(p_donor)
    new_donor = request.app.database["donors"].insert_one(j_donor)
    
    created_donor = request.app.database["donors"].find_one(
        {"_id": new_donor.inserted_id}
    )
    return created_donor


# list    
@donor_api.get("/", response_description="List all donors")
def list_donor(request: Request):
    donors = list(request.app.database["donors"].find({}))
    return donors

#delete
@donor_api.delete("/{id}", response_description="Delete a donor")
def delete_donor(id: str, request: Request, response: Response):
    delete_result = request.app.database["donors"].delete_one({"_id": id})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Author not found")
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)


#find
@donor_api.get("/{id}", response_description="Get a single donor by id")
def find_donor(id: str, request: Request):
    donor = request.app.database["donors"].find_one({"_id": id})
    return donor   
    
#UPDATE 
@donor_api.post("/{id}", response_description="Update a donor", response_model=donorUpdate)
async def update_donor(id: str, request: Request, donor: donorUpdate = Body(...)):
    j_donor = jsonable_encoder(donor)
    update_result = request.app.database["donors"].update_one(
        {"_id": id}, {"$set": j_donor}
    )
    updated_donor = request.app.database["donors"].find_one({"_id": id})    
    return updated_donor
 