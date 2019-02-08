'''
import pathlib

#   rutas 
images_drone = './images_drone'
images_database = './images_database'

# define the path
Directory_images_drone = pathlib.Path(images_drone)

for image_drone in Directory_images_drone.iterdir():  
    print(image_drone)
'''
#   librerias
import shutil
import os
import uuid
#   rutas 
images_drone = './images_drone'
images_database = './images_database'
#   listar archivos
for image_drone in os.listdir(images_drone):
    if image_drone.endswith(".jpg"):
        print(image_drone)
        uuid4 = str(uuid.uuid4())
        image_drone_rename = uuid4 + '.jpg'
        os.rename(images_drone + '/' + image_drone, images_drone + '/' + image_drone_rename)
        image_drone = image_drone_rename
        shutil.move(images_drone + '/' + image_drone , images_database)