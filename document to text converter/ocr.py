# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 17:54:17 2019

@author: HP
"""

from PIL import Image
import pytesseract
import argparse
import cv2
import os

def do_stuff(image_link,preprocess):

    image=cv2.imread(image_link)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    if preprocess=="thresh":
        gray=cv2.threshold(gray,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)[1]
    

    elif preprocess=="blur":
        gray=cv2.medianBlur(gray,3)
    
    filename="{}.png".format(os.getpid())
    cv2.imwrite(filename,gray)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text=pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    #cv2.imshow("Image",image)
   # cv2.imshow("Output",gray)
    return text



if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("-i","--image",required=True)
    ap.add_argument("-p","--preprocess",type=str,default="thresh")
    args=vars(ap.parse_args())


    print(do_stuff(args["image"],args["preprocess"]))
    
    cv2.waitKey(0)