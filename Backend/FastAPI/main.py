### HELLO FAST API ###

# Documentación oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"

from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

# Inicia el server: uvicorn main:app --reload (El path debe de estar en la carpeta que contenga el main)
# Detener el server: CTRL+C

# Documentación Automática con Swagger: http://127.0.0.1:8000/docs
# Documentación Automática con Redocly: http://127.0.0.1:8000/redoc


app = FastAPI()

### Routers ###
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)

app.mount("/static", StaticFiles(directory="static"), name="static")    # http://127.0.0.1:8000/static/images/icons8-superman-480.png


# Url local: http://127.0.0.1:8000
@app.get("/")
async def root(): 
    return "¡Hola FastAPI!"

# Url local: http://127.0.0.1:8000/url
@app.get("/url")
async def url(): 
    return {"google":"https://www.google.com/"}

