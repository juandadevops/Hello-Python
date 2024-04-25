######################
### MongoDB Client ###
######################

# Download community version: https://www.mongodb.com/try/download
# Installation: https://www.mongodb.com/docs/manual/tutorial
# MongoDB connection module: pip install pymongo
# Execution: sudo mongod --dbpath "/path/a/la/base/de/datos/"
# Connection: mongodb://localhost

from pymongo import MongoClient
from ConfigMaps import config

# Local Database
# db_client = MongoClient().local

# Remote Database
db_client = MongoClient(config.connection_string_mongodb).test