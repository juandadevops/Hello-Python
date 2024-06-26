#################
### USERS API ###
#################

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

# Router API to be able to be called from main
# General Path --> /users
router = APIRouter(prefix="/users", tags=["users"], responses={404: {"message": "Not found"}})

@router.get("/usersjson")
async def usersjson(): 
    return [{"name": "Luis", "surname": "Gil", "age":  18, "url": "https:google.com"},
            {"name": "Mario", "surname": "López", "age":  45, "url": "https:google.com"},
            {"name": "Manuel", "surname": "Ramiro", "age":  32, "url": "https:google.com"}]
    

# User Entity
class User(BaseModel):
    id: int
    name:  str
    surname: str
    age: int
    url: str

users_list = [User(id=1, name="Luis", surname="Gil", age=18, url="https:google.com"),
         User(id=2, name="Mario", surname="López", age=45, url="https:google.com"),
         User(id=3, name="Manuel", surname="Ramiro", age=32, url="https:google.com")]

@router.get("/")
async def users():
    return users_list 

# PATH
@router.get("/user/{id}")
async def uerById(id: int):
    return search_user(id)
    
# QUERY
@router.get("/userquery/")
async def user(id: int):
    return search_user(id)
    
    
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def insert_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user already exists")
    else:
        users_list.append(user)
        return user
    
    
@router.put("/", response_model=User, status_code=status.HTTP_200_OK)
async def update_user(user: User):
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
          
    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User has not been updated") 
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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User has not been deleted") 


## Auxiliary methods ##
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"Error":"User not found"}