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
  image_barcode = cv2.imread('barcode_1.jpeg')
  barcode_decode(image_barcode)