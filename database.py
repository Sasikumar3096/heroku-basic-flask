import mysql.connector
from mysql.connector import Error

from others import decode_image

connection = mysql.connector.connect(host='localhost',
                                     database='project',
                                     user='root',
                                     password='')
# connection = mysql.connector.connect(host='18.217.103.149',
#                                      database='project',
#                                      user='sasi',
#                                      password='RamSs91027')
db_Info = connection.get_server_info()
print("Connected to MySQL Server version ", db_Info)
cursor = connection.cursor()

def get_photo_from_db():
    cursor.execute("select photo from transaction order by id desc limit 1;")
    photo = cursor.fetchone()[0]

    decode_image(photo)
    return True

def get_user_info(email):
    cursor.execute(f"Select id,number from user_info where email_id like '{email}';")
    id, number = cursor.fetchone()
    print(f"User Id:{id}, Mobile_number: {number}")
    return id, number

if __name__ == "__main__":
    get_photo_from_db()
    get_user_info("thisismyinternetid@gmail.com")