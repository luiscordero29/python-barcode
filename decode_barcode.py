#   librerias
import shutil
import os
import uuid
import sqlite3
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
#   base de datos
conn = sqlite3.connect('database.db')
c = conn.cursor()


def barcode_decode(im, image_id):
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)
    for obj in decodedObjects:
        uuid4 = str(uuid.uuid4())
        barcode_type = obj.type
        barcode_data = str(obj.data, "utf-8")
        print(barcode_data)
        c.execute("INSERT INTO barcodes (barcode_id, image_id, barcode_type, barcode_data) VALUES ('"+uuid4+"', '"+image_id+"', '"+barcode_type+"', '"+barcode_data+"')")
        conn.commit()
    return decodedObjects


#   rutas
images_drone = './images_drone'
images_database = './images_database'
#   listar archivos
for image_drone in os.listdir(images_drone):
    if image_drone.endswith(".jpg"):
        print(image_drone)
        uuid4 = str(uuid.uuid4())
        image_drone_rename = uuid4 + '.jpg'
        os.rename(images_drone + '/' + image_drone,
                  images_drone + '/' + image_drone_rename)
        image_drone = image_drone_rename
        shutil.move(images_drone + '/' + image_drone, images_database)
        c.execute("INSERT INTO images (image_id, image) VALUES ('" +
                  uuid4+"', '"+image_drone+"')")
        conn.commit()
        image_barcode = cv2.imread(images_database + '/' + image_drone)
        # Read image
        barcode_decode(image_barcode, uuid4)


conn.close()
