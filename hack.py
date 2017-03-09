import cv2
from clarifai import rest
from clarifai.rest import ClarifaiApp

def capture_image(camera):
     returnval, image = camera.read() #PIL format , if returnval = true then success
     return image

def checkUser_available():
    integrated_webCam_port = 0   
    camera = cv2.VideoCapture(integrated_webCam_port) #initialise Camera Object
    throw_frames = 50    #Number of frames to throw away while the camera adjusts to light levels
      
    for i in range(throw_frames):
     captured_image = capture_image(camera)
    print("Captured Image")
    
    # Release Camera Object
    del(camera)
    
    app = ClarifaiApp("j2YUSmHm9mdHrmkyyMSCFpSCw1IIx3zklh11gBdb", "LVGCwYY5eD-v7SvADRNj3_Zfxf9WPtNJ93k4XsH8")
    model = app.models.get("e466caa0619f444ab97497640cefc4dc")
    x = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')
    
    print (x)
    file = "C:/Users/pyadav/Desktop/A/Learning/test_image.jpg"
    cv2.imwrite(file, captured_image)
     
    
    

if __name__ == "__main__":
    checkUser_available()