from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
 
def barcode_decode(im) : 
  # Find barcodes and QR codes
  decodedObjects = pyzbar.decode(im)
 
  # Print results
  for obj in decodedObjects:
    print('Type -> : ', obj.type)
    print('Data -> : ', obj.data,'\n')
     
  return decodedObjects

# Main 
if __name__ == '__main__':
 
  # Read image
  image_barcode = cv2.imread('/home/luiscordero29/Projects/Uworks/ucontrol/laravel/public/uploads/a5637c74-b23e-4d81-b2bf-a08f13cdab6c.jpg')
  barcode_decode(image_barcode)