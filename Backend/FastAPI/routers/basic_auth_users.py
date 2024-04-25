#################################################
### Users API with basic OAuth2 authorization ###
#################################################

from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(prefix="/basicauth", tags=["basicauth"], responses={404: {"message": "Not found"}})

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# User Entity
class User(BaseModel):
    username:  str
    fullname:  str
    email: str
    disabled: bool

# User DB Entity (With personal password)
class UserDB(User):
    password: str


users_db = {
    "luisdev": {
        "username":  "luisdev",
        "fullname":  "Luis Gil",
        "email": "luisgil@luisdev.com",
        "disabled": False,
        "password": "123456"
    },
    "luisdev2": {
        "username":  "luisdev2",
        "fullname":  "Luis Gil 2",
        "email": "luisgil2@luisdev.com",
        "disabled": True,
        "password": "654321"
    }
}

## Auxiliary methods ##
def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid authentication credentials", 
            headers={"WWW-Authenticate": "Bearer"})
        
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Inactive user")
    return user
    
## API Methods ##
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The username is not correct") 
    
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The password is not correct") 
    
    return {"access_token": user.username, "token_type": "bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user