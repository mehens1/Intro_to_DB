import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Establish connection to MySQL server
        cnx = mysql.connector.connect(
            user='your_username',
            password='your_password',
            host='your_host'
        )
        cursor = cnx.cursor()
        
        # Create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        # Close cursor and connection
        cursor.close()
        cnx.close()

if __name__ == "__main__":
    create_database()
