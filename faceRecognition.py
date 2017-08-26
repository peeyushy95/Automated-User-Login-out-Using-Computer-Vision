# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 00:37:14 2017

@author: pyadav
"""
import cv2
import os
import numpy as np
cascadePath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascadePath)
recognizer = cv2.face.createLBPHFaceRecognizer()

def train_model(path):
    images, labels = fetch_images_labels(path)
    for ind in range(len(labels)) :
        if labels[ind] == 'me':
            labels[ind] = 0
        else:
            labels[ind] = 1
    recognizer.train(images,np.array(labels))
    #print(images_path)
    #recognizer

def image_process(path):
     images_path = [os.path.join(path,f) for f in os.listdir(path) if not f.startswith('.')]
     for image in images_path:
        img = cv2.imread(image)
        cv2.imshow("nd",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=10,
            minSize=(30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
        )
        os.chdir("images")
        for (x, y, w, h) in faces:
            print(img.shape[0])
            temp_image = img[max(0,y-100):min(y+h+100,img.shape[1]),max(0,x-100):min(x+w+100,img.shape[0]),:]
            resized_image = cv2.resize(temp_image, (255, 320)) 
            
            cv2.imwrite("img"+str(x)+'.jpg',temp_image)    
            #cv2.imshow("image" ,resized_image)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
        os.chdir("..")
    
    
def fetch_images_labels(path):
     images_path = [os.path.join(path,f) for f in os.listdir(path) if not f.startswith('.')]
     images = []
     labels = []
     for image in images_path:
        img = cv2.imread(image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        labels.append("me")
        images.append(gray)
     return images, labels
    
def recognise_face(image):
       
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    #print(gray.shape)
    validUser = False
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        temp_image = gray[max(0,y-100):min(y+h+100,image.shape[1]),max(0,x-100):min(x+w+100,image.shape[0])]
        #resized_image = cv2.resize(temp_image, (50, 50))
        classId, conf = recognizer.predict(temp_image)
        print(classId, conf)
        if(classId == 0):
            validUser = True
            
    if(len(faces) > 0 and validUser):
        return True
    else :
        '''
        cv2.imshow("Fraud",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.waitKey(1) # fix for mac
        '''
        return False
              
    