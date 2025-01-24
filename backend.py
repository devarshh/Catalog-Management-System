import csv
import hashlib

DB_FILE = "catalog.csv"

# Hash password (use MD5 for now, replace with a secure hash in production)
def hash_password(password):
    """Hashes a password using MD5."""
    return hashlib.md5(password.encode()).hexdigest()

# Validate user credentials
def validate_login(username, password):
    """Validates user credentials from a mock database."""
    database = {
        "admin": hash_password("password"),  # Example: "password"
        "user1": hash_password("123"),      # Example: "123"
    }
    hashed_password = hash_password(password)
    return username in database and database[username] == hashed_password

# Read catalog from CSV
def read_catalog():
    try:
        with open(DB_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []

# Write catalog to CSV
def save_catalog(catalog):
    with open(DB_FILE, mode='w', newline='') as file:
        fieldnames = ["ID", "Name", "Description"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(catalog)

# Validate catalog item
def validate_item(item):
    return item.get("ID") and item.get("Name") and item.get("Description")

# Add new item
def add_item(catalog, new_item):
    if validate_item(new_item):
        catalog.append(new_item)
        return True
    return False

# Edit existing item
def edit_item(catalog, item_id, updates):
    for item in catalog:
        if str(item["ID"]) == str(item_id):
            item.update(updates)
            return True
    return False
