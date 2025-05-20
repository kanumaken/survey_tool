import os
import csv
from pymongo import MongoClient
from user_model import User
from dotenv import load_dotenv

# Load Mongo URI from .env file
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

# MongoDB connection
client = MongoClient(MONGO_URI)
db = client['survey_db']
collection = db['participants']

# Output CSV path inside current folder's 'data' directory
output_path = "data/survey_data.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Fetch data
docs = collection.find()
users = []

for doc in docs:
    user = User(
        age=doc.get("age"),
        gender=doc.get("gender"),
        total_income=doc.get("total_income"),
        expenses=doc.get("expenses", {})
    )
    users.append(user)

# Define CSV headers
fieldnames = ["age", "gender", "total_income", "utilities", "entertainment", "school_fees", "shopping", "healthcare"]

# Write to CSV
with open(output_path, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for user in users:
        writer.writerow(user.to_dict())

print(f"[✓] Exported {len(users)} records to {output_path}")
