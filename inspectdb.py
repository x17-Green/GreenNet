from app import db

# Inspect the database schema
print(db.metadata.tables)

# Inspect the data in a specific table
print(db.session.query(User).all())