### HELLO FAST API ###

# Documentación oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"

from fastapi import FastAPI

# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación Automática con Swagger: http://127.0.0.1:8000/docs
# Documentación Automática con Redocly: http://127.0.0.1:8000/redoc


app = FastAPI()

# Url local: http://127.0.0.1:8000
@app.get("/")
async def root(): 
    return "¡Hola FastAPI!"

# Url local: http://127.0.0.1:8000/url
@app.get("/url")
async def url(): 
    return {"google":"https://www.google.com/"}

