###############################################
### Users API with OAuth2 authorization JWT ###
###############################################

from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from Secrets import secret

ALGORITHM = secret.algorithm_jwt
ACCESS_TOKEN_DURATION = 1
SECRET = secret.secret_token_jwt

router = APIRouter(prefix="/jwtauth", tags=["jwtauth"], responses={404: {"message": "Not found"}})

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

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
        "password": "$2a$12$Ei/lTky7bWvfI4JxJMdb6OfFEu.Lei8ZzwRL5KcY/JYD0MbwYEI2i"
    },
    "luisdev2": {
        "username":  "luisdev2",
        "fullname":  "Luis Gil 2",
        "email": "luisgil2@luisdev.com",
        "disabled": True,
        "password": "$2a$12$g3WNcAjSkiEL9a/PIhTD8.w0cNdl/7fVftmD6DX7xxiKaHZx4qUa6"
    }
}

## Auxiliary methods ##
def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    
async def auth_user(token: str = Depends(oauth2)):
    
    exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid authentication credentials", 
            headers={"WWW-Authenticate": "Bearer"})
    
    try :
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception  
        
    except JWTError:
        raise exception
    
    return search_user(username)
    
async def current_user(user: User = Depends(auth_user)):    
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
    
    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The password is not correct") 
    
    access_token_expiration = timedelta(minutes=ACCESS_TOKEN_DURATION)
    expire_date = datetime.utcnow() + access_token_expiration
    access_token = {"sub": user.username, 
                    "exp": expire_date}
    
    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user