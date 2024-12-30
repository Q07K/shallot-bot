from pymongo import MongoClient

from config import (
    MONGODB_HOST,
    MONGODB_PASSWORD,
    MONGODB_PORT,
    MONGODB_USERNAME,
)

MONGODB_CLIENT = MongoClient(
    host=MONGODB_HOST,
    port=MONGODB_PORT,
    username=MONGODB_USERNAME,
    password=MONGODB_PASSWORD,
)
