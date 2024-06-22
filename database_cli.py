from pymongo import MongoClient

# Connection details
host = 'localhost'    # or the IP address of the MongoDB server
port = 27017          # default MongoDB port
username = 'admin'
password = 'admin'
database_name = 'admin'
collection_name = 'content'

# Create a MongoClient with authentication
client = MongoClient(
    host=host,
    port=port,
    username=username,
    password=password,
    authSource=database_name  # the database to authenticate against
)

# Select the database
db = client[database_name]

# Select the collection
collection = db[collection_name]

# Data to be inserted
data = {
  "_id": "66768e828c1a8f5a2f00b2b6",
  "title": "Semiconductor Processing Overview",
  "menu": [
    "Tutorial",
    "Course Overview",
    "General Overview",
    "Technical Overview"
  ],
  "footer": [
    "Glossary",
    "About SPO"
  ],
  "image": "SPOA.png"
}

# Insert the data
result = collection.insert_one(data)

# Output the ID of the inserted document
print("Inserted document ID:", result.inserted_id)
