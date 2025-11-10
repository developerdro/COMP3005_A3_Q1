import psycopg2

DB_HOST = "localhost"
DB_PORT = "5432"
DB_USER = "postgres"
DB_PASS = ""
DB_NAME = "University"

# Connects to database 
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host = DB_HOST,
            port = DB_PORT,
            user = DB_USER,
            password = DB_PASS,
            database = DB_NAME,
        )
        return conn

    except Exception as e:
        print(f"Error connecting to databse: {e}")
        return None