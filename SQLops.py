#pip install mysql-connector-python streamlit

import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",         # Default MySQL username in XAMPP
    password="",         # Default MySQL password in XAMPP (leave empty if not set)
)

cursor = conn.cursor()

# Create a new database
cursor.execute("CREATE DATABASE IF NOT EXISTS file_management_db")

# Select the newly created database
cursor.execute("USE file_management_db")

# Create the usertable
cursor.execute('''
CREATE TABLE IF NOT EXISTS usertable (
    userid INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
)
''')

# Create the data_entry table
cursor.execute('''
CREATE TABLE IF NOT EXISTS data_entry (
    id INT AUTO_INCREMENT PRIMARY KEY,
    userid INT,
    filename VARCHAR(255) NOT NULL,
    ipfs_storage_link VARCHAR(255) NOT NULL,
    file_description TEXT,
    file_key VARCHAR(255) NOT NULL,
    FOREIGN KEY (userid) REFERENCES usertable(userid)
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and tables created successfully!")
import mysql.connector

# Database connection function
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # Default MySQL username in XAMPP
        password="",         # Default MySQL password in XAMPP (leave empty if not set)
        database="file_management_db"
    )

# CREATE: Insert a new user into the usertable
def create_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO usertable (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        print("User created successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# READ: Retrieve a user by username
def read_user(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usertable WHERE username = %s", (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

# UPDATE: Update a user's password
def update_user_password(username, new_password):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE usertable SET password = %s WHERE username = %s", (new_password, username))
        conn.commit()
        print("Password updated successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# DELETE: Delete a user by username
def delete_user(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM usertable WHERE username = %s", (username,))
        conn.commit()
        print("User deleted successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# CREATE: Insert a new file entry into the data_entry table
def create_file_entry(userid, filename, ipfs_storage_link, file_description, file_key):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO data_entry (userid, filename, ipfs_storage_link, file_description, file_key) 
            VALUES (%s, %s, %s, %s, %s)
        """, (userid, filename, ipfs_storage_link, file_description, file_key))
        conn.commit()
        print("File entry created successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# READ: Retrieve file entries for a specific user
def read_file_entries(userid):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data_entry WHERE userid = %s", (userid,))
    files = cursor.fetchall()
    cursor.close()
    conn.close()
    return files

# UPDATE: Update the IPFS storage link for a file entry
def update_file_link(file_id, new_ipfs_storage_link):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE data_entry SET ipfs_storage_link = %s WHERE id = %s", (new_ipfs_storage_link, file_id))
        conn.commit()
        print("IPFS storage link updated successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# DELETE: Delete a file entry by its ID
def delete_file_entry(file_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM data_entry WHERE id = %s", (file_id,))
        conn.commit()
        print("File entry deleted successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# Example usage of CRUD operations
if __name__ == "__main__":
    # User operations
    create_user("user1", "password1")
    create_user("user2", "password2")
    
    user = read_user("user1")
    print(f"Read user: {user}")
    
    update_user_password("user1", "newpassword1")
    
    delete_user("user2")
    
    # File entry operations
    create_file_entry(1, "file1.txt", "ipfs://example1", "This is file 1", "key1")
    create_file_entry(1, "file2.txt", "ipfs://example2", "This is file 2", "key2")
    
    files = read_file_entries(1)
    print(f"File entries for user 1: {files}")
    
    update_file_link(1, "ipfs://newlink1")
    
    delete_file_entry(2)
