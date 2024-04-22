####################
### USERS DB API ###
####################

from fastapi import APIRouter, HTTPException, status
from database.models.user import User
from database.schemas.user import user_schema, users_schema
from database.client import db_client
from bson import ObjectId

router = APIRouter(prefix="/usersdb", tags=["usersdb"], responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


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
    # TODO: COMPROBAR PORQUE ME PIDE EL ID A LA HORA DE HACER EL POST SI LO HE PUESTO "NONE" (OPCIONAL)
    
    id = db_client.local.users.insert_one(user_dict).inserted_id
    new_user = user_schema(db_client.local.users.find_one({"_id": id}))
    
    
    return User(**new_user)
    
    
@router.put("/", response_model=User, status_code=status.HTTP_200_OK)
async def update_user(user: User):

    user_dict = dict(user)
    del user_dict["id"]

    try:     
        db_client.local.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)
    except:
        return {"Error":"No se ha encontrado el usuario"}

    return search_user("_id", ObjectId(user.id))
    
    
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: str):
    
    found = db_client.local.users.find_one_and_delete({"_id": ObjectId(id)})     
          
    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se ha eliminado el usuario") 


def search_user(field: str, key):
    try:
        user = db_client.local.users.find_one({field: key})
        return User(**user_schema(user))
    except:
        return {"Error":"No se ha encontrado el usuario"}






