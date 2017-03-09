__author__ = 'pyadav'

import cv2
import ctypes 
import time
import platform
#from clarifaiClientSetup import predictUserAvailable  #Required, if using Clarifai API 
from faceRecognition import recognise_face

integrated_webCam_port = 0
throw_frames = 50   #Number of frames to throw away while the camera adjusts to light levels
file = "C:/Users/pyadav/Desktop/A/Learning/test_image.jpg"


def capture_image():
    camera = cv2.VideoCapture(integrated_webCam_port) #initialise Camera Object
    for i in range(throw_frames):
        returnval, image = camera.read() #PIL format , if returnval = true then success
    camera.release();                                  # Release Camera Object
    print(image)
    return image

def checkUser_available_fixedInterval(sleep_time):
        
    while True :
        time.sleep(sleep_time)
        captured_image = capture_image()
        print("Captured Image")
               
        '''
        Required if using Clarifai API 
        cv2.imwrite(file, captured_image) #REquired if Using Clarifai Api
        if(predictUserAvailable(file)== False):
        '''    
        if( recognise_face(captured_image) == False):
            print("User Not Available")
            find_OS_toLock()
            break;
        else:
            print("User Available")
            
def checkUser_available_continuous():   
    camera = cv2.VideoCapture(integrated_webCam_port) #initialise Camera Object
    
        
def find_OS_toLock():
    os_type = platform.system()
    if(os_type == 'Windows'):
        user32 = ctypes.cdll.LoadLibrary("user32.dll") 
        user32.LockWorkStation()
    elif (os_type == 'Darwin') :
        #do Nothing
        os_type = 'Darwin'

 
def release_Camera():
    camera = cv2.VideoCapture(0) #initialise Camera Object       
    del(camera)
        
if __name__ == "__main__":
    
    sleep_time = 2  
    #release_Camera() # FIx : Run this function if camera doesnt turn off.
    checkUser_available_continuous()
    checkUser_available_fixedInterval(sleep_time)
