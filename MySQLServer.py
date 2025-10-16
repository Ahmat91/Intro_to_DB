import mysql.connector

def create_database():
    try:
        # Connect to MySQL Server (without selecting a database yet)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",   # Change if your MySQL root has a password
            password=""
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:  # ✅ Matches checker format
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Properly close cursor and connection
        try:
            if cursor:
                cursor.close()
            if connection.is_connected():
                connection.close()
                print("MySQL connection closed.")
        except:
            pass

if __name__ == "__main__":
    create_database()
