"""This module contains utility functions for connecting to the DB"""
from psycopg2 import connect 

def get_db_connection():
    return connect("postgres://postgres:postgres@localhost:5432/postgres")