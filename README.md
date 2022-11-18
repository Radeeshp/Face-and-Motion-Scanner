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

#### Working:
        -This is the driver code of the project.
        -In Facescanner.py we get the input mp4 file location. 
        -Then the image is cleaned and motion is detected.
        -When motion is detected we save the first few frames and then we check 
        to see if we can detect a face or any parts of the face. 
        -When a face or part of the face (eye,ear,nose) is detected we save the image frame 
        in a location given by the user.
        -The frame is saved with the time it was taken.
        
        
#### Activity Diagram:

![1_page-0001 (1)](https://user-images.githubusercontent.com/82216452/202774705-88925f3b-f034-459c-8605-847255fedcc5.jpg)

        

#### Imports Used: 
        -import cv2
      
#### Built In Functions Used:
        -cv2.contourArea(contours)
        -cv2.boundingRect(contours)
        -cv2.rectangle(frame,(x,y),(x+w,y+h),(0,55,55),2)
        -cv2.imwrite("frame%d.jpg" % i, frame)
#### def Facescanner():

## References:
      -Google 
      -pyimagesearch
      -OpenCv
      -https://www.researchgate.net/publication/343127730_Face_Detection_Using_OpenCV_and_Haar_Cascades_Classifiers
      -https://www.ijser.org/researchpaper/Motion-detection-algorithm-based-on-Background-Subtraction.pdf
      
