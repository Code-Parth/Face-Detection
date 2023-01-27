# Face-Detection

``haarcascade_frontalface_default.xml``

haarcascade_frontalface_default.xml is a pre-trained classifier file in the XML file format. It is used to detect frontal faces in an image using the Haar cascade algorithm. This file is part of the OpenCV library and can be used in conjunction with other OpenCV functions to perform facial detection and recognition tasks. The Haar cascade algorithm works by training a classifier on thousands of positive and negative images, and then using that classifier to detect objects in new images. The haarcascade_frontalface_default.xml file is trained to detect frontal faces, and can be used as a starting point for building more advanced facial recognition systems.

-----

``Face_Detection.py``

This script is using the OpenCV library to perform facial recognition. It first loads in a set of images from a specified directory and runs the Haar cascades classifier to detect and extract the faces from the images. It then calculates the mean value of each face and appends it to an array, "face_features." The script then takes the mean of all the face features and assigns it to a template variable. The script then captures video from the user's webcam and runs the same Haar cascades classifier on each frame of the video. It then compares the mean value of each detected face in the video frame with the template and if the difference is less than 100, it displays a message saying "match found!" otherwise "No match found." The script continues to do this until the user presses the 'q' key to quit.

-----

``Take_Video.py``

This script captures video from the default camera (camera index 0), sets the resolution of the video to 640x480, discards the first 5 frames to allow the camera to adjust to the lighting conditions, and then captures video for an unspecified amount of time (until the user presses the 'q' key). The captured frames are saved to a file named "output.avi" in the same directory as the script using the XVID codec. The frames are also displayed in a window named "Camera Feed". Once the user presses the 'q' key or the video capture fails, the script releases the camera and video writer objects, and closes all open windows.

-----

``Video_To_PNG.py``

This code captures a video file named 'output.avi' using the cv2 library's VideoCapture function. It then retrieves the total number of frames in the video using the CAP_PROP_FRAME_COUNT property, and initializes a variable 'frame_idx' to 0. Then it enters a while loop that reads each frame of the video and saves it as an image file with a file name in the format 'images/XXX.png' where XXX is the value of the frame_idx variable incremented by 1 in each iteration. If the read() function returns False, the loop breaks, and the video capture is released using the release() function.

-----

``main.py``

This script uses the OpenCV library to create a class for face recognition. The class, called FaceRecognizer, takes in two parameters: an image_dir where the images of known faces are stored, and a cascade_path where the Haar cascade classifier XML file is located. The class initializes with the creation of a template of known faces. The create_template method reads all the images in the image_dir and converts them to grayscale. It then uses the Haar cascade classifier to detect faces in the images and creates a list of the detected faces. The method then calculates the mean value of the pixels of each face image, and takes the mean of all the face features to create the template. The recognize method captures video from the default camera and converts it to grayscale. It uses the Haar cascade classifier to detect faces in the video frames and calculates the mean value of the pixels of the detected face. It then compares the calculated mean value of the new face with the template and if the euclidean distance between them is less than 100, it displays the message "Match found!" else "No match found." on the video frames. The script then creates an instance of the FaceRecognizer class and calls the recognize method on it.

-----

# Overview

This code contains several scripts that use the OpenCV library to perform facial recognition tasks. The haarcascade_frontalface_default.xml file is a pre-trained classifier that uses the Haar cascade algorithm to detect frontal faces in an image. The Face_Detection.py script loads in a set of images and uses the classifier to detect and extract the faces from the images, calculating the mean value of each face and creating a template. The Take_Video.py script captures video from the default camera and saves it to a file named "output.avi". The Video_To_PNG.py script converts the "output.avi" video file into a series of PNG images. The main.py script creates a FaceRecognizer class that takes in an image_dir and cascade_path as parameters and uses them to create a template of known faces. It captures video from the default camera and uses the Haar cascade classifier to detect faces in the video frames, comparing the calculated mean value of the new face with the template and displaying a message if a match is found.

-----
