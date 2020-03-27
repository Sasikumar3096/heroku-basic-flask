import base64
import tempfile
import os
import shutil
from PIL import Image
import io


def create_folder():
    try:
        shutil.rmtree('temp/')
    except Exception as e:
        print(e)
    try:
        os.mkdir("temp")
    except Exception as e:
        print(e)


def decode_image(image):

    print("Inside Decode Image")
    base64_img_bytes = base64.b64decode(image[23:])
    try:
        create_folder()
        with open('temp/images.png', 'wb') as file_to_save:
            decoded_image_data = base64_img_bytes
            file_to_save.write(decoded_image_data)

        print(os.path.abspath(os.getcwd())+ "temp/images.png")
    except:
        decode_image(image)