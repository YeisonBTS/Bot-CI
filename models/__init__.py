from pymongo import MongoClient
from user import User


URL = 'localhost'
PORT = 27017
USER_COLLECTION = 'users'

client = MongoClient(URL, PORT)
database = client.bot

UserModel = User(database, USER_COLLECTION)