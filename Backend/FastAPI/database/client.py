### MongoDB Client ###

# Descarga versión community: https://www.mongodb.com/try/download
# Instalación:https://www.mongodb.com/docs/manual/tutorial
# Módulo conexión MongoDB: pip install pymongo
# Ejecución: sudo mongod --dbpath "/path/a/la/base/de/datos/"
# Conexión: mongodb://localhost


from pymongo import MongoClient

# Base de datos local
# db_client = MongoClient().local


# Base de datos remota
db_client = MongoClient("mongodb+srv://test:test@cluster0.lz0usti.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").test