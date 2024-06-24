#!/usr/bin/python3
# Script that creates a database

from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        print("Login to create a database"),
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        create_db_query = "CREATE DATABASE online_movie_rating"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
except Error as e:
    print(e)
