# Theft Scanner

A python and computer vision project to detect faces and motion and store the faces that have been detected

## Problem Statement:
      Generally when someone wants to review a footage and needs to find who  
      and when someone went past a camera(Security Camera) they have to review the 
      whole footage but using this project they can simplify this process.
      
      All they would have to do is upload the video file or give the video  file's 
      location and they would get the photos of all  the faces that entered the frame
      it would also show the first few image frames when some motion is detected.
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
        -When a face or part of the face (ear) is detected we save the image frame 
        (We are detecting the ear also as we ahve to be able to detect the face even if 
        the face is not straight) in a location given by the user.
        -The frame is saved with the time it was taken.
        
        
#### Activity Diagram:
![1_page-0001 (1)](https://user-images.githubusercontent.com/82216452/202778989-b326eff1-2023-4144-93e7-b0b181a48f71.jpg)

        

#### Imports Used: 
        -import cv2
      
#### Built In Functions Used:
        -cv2.contourArea(contours)
        -cv2.boundingRect(contours)
        -cv2.rectangle(frame,(x,y),(x+w,y+h),(0,55,55),2)
        -cv2.imwrite("frame%d.jpg" % i, frame)
        -cv2.imshow()
        -cv2.dilate()
        -cv2.findContours()
        -cv2.CascadeClassifier()
        -faceCascade.detectMultiScale()
        -cv2.cvtColor()
        -video_capture.release()
        -cv2.GaussianBlur()
        -cv2.destroyAllWindows()
#### def Facescanner():
        -This is a user defined function thats used to find whether there is any motion and or faces in the image
        -We detect motion using background subtraction
        -When motion has been detected we try to detect face or parts of the faces 
        -if thereare face faces or parts of the face detected we return true 
##### Activity Diagram:
![kl_page-0001](https://user-images.githubusercontent.com/82216452/202844420-15aa7b93-d364-4499-9889-ac2055232955.jpg)


## References:
      -Google 
      -pyimagesearch
      -OpenCv
      -https://www.researchgate.net/publication/343127730_Face_Detection_Using_OpenCV_and_Haar_Cascades_Classifiers
      -https://www.ijser.org/researchpaper/Motion-detection-algorithm-based-on-Background-Subtraction.pdf
      
