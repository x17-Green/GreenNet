#!/usr/bin/python3
# MySQL Database connector

from sqlalchemy import create_engine, text  # type: ignore
from dotenv import load_dotenv
import os

# # Database Connection Parameters
# username = 'green'
# password = 'root'
# host = 'localhost'
# port = 3306 # default MySQL port
# database = 'greennet_db'

# # Connection string
# db_url = f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}'

# # Access to engine
# engine = create_engine(db_url, echo=True)

# # Test the connection
# try:
#     connection = engine.connect()
#     print("Connected to the database!")
# except Exception as e:
#     print(f"Error connecting to the database: {e}")

# # AS A FUNCTION
# def database_connect(username, password, host, port, database):
#     """
#     Connect to a MySQL database using SQLAlchemy.

#     Args:
#         username (str): MySQL username
#         password (str): MySQL password
#         host (str): MySQL host
#         port (int): MySQL port
#         database (str): MySQL database name

#     Returns:
#         engine (Engine): SQLAlchemy Engine object
#     """

#     # Connection string
#     db_url = (f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}'

#     # Access to the engine
#     engine = create_engine(db_url)

#     try:
#         connection = engine.connect()
#         print("Connecting to the database...!")
#         return engine
#     except Exception as e:
#         print(f"Error connecting to the database: {e}")
#         return None


# # Test the function
# def test_database_connect():
#     username = 'green'
#     password = 'root'
#     host = 'localhost'
#     port = 3306 # default MySQL port
#     database = 'greennet_db'

#     engine = database_connect(username, password, host, port, database)
#     if engine:
#         print("Connection successful!")
#     else:
#         print("Connection failed!")

# test_database_connect()

###
###
###


# USING .env FILE CREDENTIALS

load_dotenv()  # Load the .env file

DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_USERPASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = int(os.getenv('DB_PORT'))
DB_NAME = os.getenv('DB_NAME')

# Create and access the engine
engine = create_engine(
    f'mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@'
    f'{DB_HOST}:{DB_PORT}/{DB_NAME}'
    )

try:
    connection = engine.connect()
    print("Connected to the database...!")
    print("\nList of Databases\n=====================\n")
    query = text("SHOW DATABASES")
    result = connection.execute(query)
    for row in result:
        print(row)
except Exception as e:
    print(f"Error connecting to the database: {e}")
finally:
    connection.close()