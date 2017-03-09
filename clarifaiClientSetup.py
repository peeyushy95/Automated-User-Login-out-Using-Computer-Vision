# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 00:37:14 2017

@author: pyadav
"""

from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import ctypes 
CLARIFAI_APP_ID = "j2YUSmHm9mdHrmkyyMSCFpSCw1IIx3zklh11gBdb"
CLARIFAI_APP_SECRET = "LVGCwYY5eD-v7SvADRNj3_Zfxf9WPtNJ93k4XsH8"
CELEBRITY_MODEL = "e466caa0619f444ab97497640cefc4dc"
# APi Setup
app = ClarifaiApp( CLARIFAI_APP_ID, CLARIFAI_APP_SECRET);
                 


def predictUserAvailable(file):
    model = app.models.get(CELEBRITY_MODEL)
    image = ClImage(file_obj=open(file, 'rb'))
    response = model.predict([image])
    
    if(response['outputs'][0]['data']['regions'] == None):
        return False;
    else:
        return True;