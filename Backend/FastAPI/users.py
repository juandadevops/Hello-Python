from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Inicia el server: uvicorn users:app --reload


@app.get("/usersjson")
async def usersjson(): 
    return [{"name": "Luis", "surname": "Gil", "age":  18, "url": "https:google.com"},
            {"name": "Mario", "surname": "López", "age":  45, "url": "https:google.com"},
            {"name": "Manuel", "surname": "Ramiro", "age":  32, "url": "https:google.com"}]
    
    
    

# Entidad User
class User(BaseModel):
    id: int
    name:  str
    surname: str
    age: int
    url: str

users_list = [User(id=1, name="Luis", surname="Gil", age=18, url="https:google.com"),
         User(id=2, name="Mario", surname="López", age=45, url="https:google.com"),
         User(id=3, name="Manuel", surname="Ramiro", age=32, url="https:google.com")]

@app.get("/users")
async def users():
    return users_list 

# PATH
@app.get("/user/{id}")
async def uerById(id: int):
    return search_user(id)
    

# QUERY
@app.get("/userquery/")
async def user(id: int):
    return search_user(id)
    
    
    
@app.post("/user/")
async def insert_user(user: User):
    if type(search_user(user.id)) == User:
        return {"Error":"El usuario ya existe"}
    else:
        users_list.append(user)
        return user
    
    
@app.put("/user/")
async def update_user(user: User):
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
          
    if not found:
        return {"Error":"No se ha actualizado el usuario"} 
    else:
        return user
    
    
@app.delete("/user/{id}")
async def delete_user(id: int):
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
          
    if not found:
        return {"Error":"No se ha eliminado el usuario"} 


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"Error":"No se ha encontrado el usuario"}


