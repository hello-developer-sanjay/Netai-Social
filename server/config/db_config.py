from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the MongoDB URI from the environment variables
MONGODB_URI = os.getenv("MONGODB_URI")

# Create a MongoDB client using the URI
client = MongoClient(MONGODB_URI)

# Use the client to get the database
db = client['mydb']
