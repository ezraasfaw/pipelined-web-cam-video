# Import necessary libraries
import cv2
from PIL import Image, ImageFilter, ImageOps
import numpy as np

# Function to initialize the webcam
def initializeWebCam():
    videoDevice = cv2.VideoCapture(0, cv2.CAP_DSHOW) # Open the webcam device using OpenCV
    return videoDevice

# Function to terminate the webcam
def terminateWebCam(videoDevice):
    videoDevice.release() # Release the webcam device

# Function to capture an image from the webcam
def getImage(videoDevice):
    return_code, cvImage = videoDevice.read() # Read an image from the webcam
    if return_code==False: # If reading the image failed, exit the program
        exit(-1)
    return Image.fromarray(cvImage) # Convert the image from OpenCV format to PIL format and return it

# Function to apply an emboss filter to an image
def embossFilter(npImage):
    npImageGray = ImageOps.grayscale(npImage) # Convert the image to grayscale
    npImage_emboss = npImageGray.filter(ImageFilter.EMBOSS) # Apply the emboss filter
    return npImage_emboss # Return the filtered image

# Function to equalize the histogram of an image
def equalizeFilter(npImage):
    return ImageOps.equalize(npImage) # Equalize the image histogram and return the result

# Function to invert the colors of an image
def invertFilter(npImage):
    return ImageOps.invert(npImage) # Invert the image colors and return the result

# Function to display an image
def showImage(npImage):
    npImage = np.uint8(npImage) # Convert the image to 8-bit unsigned integer format
    cv2.imshow('Output', npImage) # Display the image in a window titled 'Output'

# Function to apply a pipeline of filters to an image
def prccessingPipeline(npImage, Pipeline):
    for filter in Pipeline: # For each filter in the pipeline
        npImage = filter(npImage) # Apply the filter to the image
    return npImage # Return the processed image

# Main function
if __name__ == '__main__':
    PipelineA = [embossFilter, equalizeFilter, invertFilter] # Define pipeline A
    PipelineB = [equalizeFilter, invertFilter] # Define pipeline B
    PipelineC = [embossFilter, equalizeFilter] # Define pipeline C

    Pipeline = PipelineA # Set the current pipeline to A
    webcam = initializeWebCam() # Initialize the webcam
    while True: # Main loop
        videoFrame = getImage(webcam) # Capture an image from the webcam
        videoFrame = prccessingPipeline(videoFrame, Pipeline) # Apply the current pipeline to the image
        showImage(videoFrame) # Display the processed image
        keypress = cv2.waitKey(1) & 0xFF # Wait for a keypress
        if keypress == ord('q'): # If 'q' is pressed, break the loop
            break
        elif keypress == ord('a'): # If 'a' is pressed, set the current pipeline to A
            Pipeline = PipelineA
        elif keypress == ord('b'): # If 'b' is pressed, set the current pipeline to B
            Pipeline = PipelineB
        elif keypress == ord('c'): # If 'c' is pressed, set the current pipeline to C
            Pipeline = PipelineC
    terminateWebCam(webcam) # Terminate the webcam
    cv2.destroyAllWindows() # Destroy all OpenCV windows
