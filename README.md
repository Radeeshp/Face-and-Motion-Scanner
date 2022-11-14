# Face-and-Motion-Scanner

A python and computer vision project to detect faces and motion and store the faces that have been detected

## Problem Statement:
      Generally when someone wants to review a footage and needs to find who  and when someone went past a camera(Security Camera) 
      they have to review the hole footage but using this project they can simplify this process . 
## Requirements:
      -computer
      -python
      -cv2
      -Video Footage
      -HaarCascade files as required
## Steps To Run The Code:
        -Install the required packages 
        -Dont change the project structure
        -Run the code using a code editor
        -Enter the video file Location
        -Enter the location to store the image file
        
## Project Structure:
        -Cascade Files
        -Facescanner.py
### Facescanner.py:

### Imports Used: 
        -import cv2
      
### Built In Functions Used:
        -cv2.contourArea(contours)
        -cv2.boundingRect(contours)
        -cv2.rectangle(frame,(x,y),(x+w,y+h),(0,55,55),2)
        -cv2.imwrite("frame%d.jpg" % i, frame)
### def Facescanner():

## References:
      -Google 
      -pyimagesearch
      -OpenCv
