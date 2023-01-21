
from asyncio.windows_events import NULL
import cv2
import sys
from cv2 import CascadeClassifier
import numpy as np

def convert_seconds_to_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, remainder = divmod(remainder, 60)
    seconds, milliseconds = divmod(remainder, 1)
    milliseconds = int(milliseconds * 1000)
    return "%d.%d.%d.%d" % (int(hours), int(minutes), int(seconds),milliseconds)

def detectfaces(frame_count,gray,first_frame):
    cascPath = ["P:\EDUCATION\PROJECTS\POLICE\haarcascade_profileface.xml","P:\EDUCATION\PROJECTS\POLICE\haarcascade_frontalface_default.xml","P:\EDUCATION\PROJECTS\POLICE\haarcascade_mcs_rightear.xml","P:\EDUCATION\PROJECTS\POLICE\haarcascade_mcs_leftear.xml"]
    delta_frame=cv2.absdiff(first_frame,gray)
    cv2.imshow('delta_frame',delta_frame)
    thresh_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    cv2.imshow('thresh',thresh_frame)
    thresh_frame=cv2.dilate(thresh_frame,None,iterations=2)
    (cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    motion=0
    for contours in cnts:
        if cv2.contourArea(contours)< 5000 :
            continue
        motion=1
        (x,y,h,w)=cv2.boundingRect(contours)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

        for j in cascPath:
            
            faceCascade=cv2.CascadeClassifier(j)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.01,#If scale factor is greater the faster the program is
                minNeighbors=14,
               
            )
            if len(faces)!=0:
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)  
                return True,motion
  
            
        

    return False,motion
    

print("**********************You Have Accessed The Facial And Motion Scannner and Detector*******************************")
#print("Enter the video file location")
#location_input=input()
print("Enter the location to store the images")
location_output=input()
frame_count=0
video_capture = cv2.VideoCapture(0)
fps = video_capture.get(cv2.CAP_PROP_FPS)
first_frame=None
frame_count_act=0
while True:
    # Capture frame-by-frame
    motion_frame=10
    frame_count_act+=1
    frame_count+=1
    check,frame=video_capture.read()
    
    if not check:
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    
    if first_frame is None:
        first_frame=gray
        continue
  
    time=str(convert_seconds_to_time(frame_count_act/fps))
    faces,motion=detectfaces(frame_count,gray,first_frame)
    #not saving frame when trying to save the timstamp as the name  
    if faces==True:
        #Due to the way the name is saved only one frame is saved for each second
        cv2.imwrite(location_output+time+".jpg", frame)
    elif motion==1 and motion_frame>0:
        motion_frame-=motion_frame
        cv2.imwrite(location_output+time+".jpg", frame)
    else :
        motion=10
        if(frame_count>1000):
            first_frame=gray
            frame_count=0
        # Display the resulting frame
    cv2.imshow('Video', frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
