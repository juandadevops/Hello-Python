#############################
### FAST API MINI PROJECT ###
#############################

# Official documentation: https://fastapi.tiangolo.com/es/

# FastAPI installation: pip install "fastapi[all]"

from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

# Start the server: uvicorn main:app --reload (The path must be in the folder containing main)
# Stop the server: CTRL+C

# Automatic Documentation with Swagger: http://127.0.0.1:8000/docs
# Automatic Documentation with Redocly: http://127.0.0.1:8000/redoc


app = FastAPI()

#############
## Routers ##
#############
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)

app.mount("/static", StaticFiles(directory="static"), name="static")    # http://127.0.0.1:8000/static/images/icons8-superman-480.png


# Local URL: http://127.0.0.1:8000
@app.get("/")
async def root(): 
    return "¡Hola FastAPI!"

# Local URL Test: http://127.0.0.1:8000/url
@app.get("/url")
async def url(): 
    return {"google":"https://www.google.com/"}

