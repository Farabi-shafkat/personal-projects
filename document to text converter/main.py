# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 01:08:39 2019

@author: HP
"""

import ocr
import argparse
import os

ap=argparse.ArgumentParser()
ap.add_argument("-i1","--image1",required=True)
ap.add_argument("-i2","--image2",required=True)
ap.add_argument("-i3","--image3",required=True)
ap.add_argument("-p","--preprocess",type=str,default="thresh")
args=vars(ap.parse_args())
text1=ocr.do_stuff(args["image1"],args["preprocess"])
text2=ocr.do_stuff(args["image2"],args["preprocess"])
text3=ocr.do_stuff(args["image3"],args["preprocess"])
print(text1)
print(text2)
print(text3)