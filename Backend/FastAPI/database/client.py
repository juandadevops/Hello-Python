### MongoDB Client ###

# Descarga versión community: https://www.mongodb.com/try/download
# Instalación:https://www.mongodb.com/docs/manual/tutorial
# Módulo conexión MongoDB: pip install pymongo
# Ejecución: sudo mongod --dbpath "/path/a/la/base/de/datos/"
# Conexión: mongodb://localhost


from pymongo import MongoClient
from ConfigMaps import config

# Base de datos local
# db_client = MongoClient().local


# Base de datos remota
db_client = MongoClient(config.connection_string_mongodb).test