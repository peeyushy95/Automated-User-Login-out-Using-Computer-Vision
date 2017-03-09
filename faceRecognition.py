# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 00:37:14 2017

@author: pyadav
"""
import cv2

print("Warning ---> Change File and Cascade Path if code is not working")
file = "C:/Users/pyadav/Desktop/A/Learning/test_image.jpg"
cascadePath = "C:/Anaconda2/envs/py35/Library/etc/haarcascades/haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascadePath)

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
        
    print ("Found {0} faces!".format(len(faces)))
    
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    #cv2.imshow("Faces found" ,image)
    #cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    if (len(faces) > 0 ):
        return True
    else :
        return False
        
def recognise_face_continuous(camera):
    
    while True : 
        returnval, image = camera.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
        )
            
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        cv2.imshow("Faces found" ,image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
        
      
#recognise_face(file)