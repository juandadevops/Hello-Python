####################
### USERS DB API ###
####################

from fastapi import APIRouter, HTTPException, status
from database.models.user import User
from database.schemas.user import user_schema, users_schema
from database.client import db_client
from bson import ObjectId

router = APIRouter(prefix="/usersdb", tags=["usersdb"], responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

users_list = []

@router.get("/", response_model=list[User])
async def users():
    return users_schema(db_client.local.users.find())

# PATH
@router.get("/{id}")
async def uerById(id: str):
    return search_user("_id", ObjectId(id))
    

# QUERY
@router.get("/userquery/")
async def user(id: str):
    return search_user("_id", ObjectId(id))
    
    
    
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def insert_user(user: User):
    if type(search_user("username", user.username)) == User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")
    
    user_dict = dict(user)
    del user_dict["id"]
    
    id = db_client.local.users.insert_one(user_dict).inserted_id
    new_user = user_schema(db_client.local.users.find_one({"_id": id}))
    
    
    return User(**new_user)
    
    
@router.put("/", response_model=User, status_code=status.HTTP_200_OK)
async def update_user(user: User):
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
          
    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se ha actualizado el usuario") 
    else:
        return user
    
    
@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_user(id: int):
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
          
    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se ha eliminado el usuario") 


def search_user(field: str, key):
    try:
        user = db_client.local.users.find_one({field: key})
        return User(**user_schema(user))
    except:
        return {"Error":"No se ha encontrado el usuario"}






