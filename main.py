import cv2
from PIL import Image, ImageFilter, ImageOps
import numpy as np

def initializeWebCam():
    videoDevice = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    return videoDevice

def terminateWebCam(videoDevice):
    videoDevice.release()

def getImage(videoDevice):
    return_code, cvImage = videoDevice.read()
    if return_code==False:
        exit(-1)
    return Image.fromarray(cvImage)

def embossFilter(npImage):
    npImageGray = ImageOps.grayscale(npImage)
    npImage_emboss = npImageGray.filter(ImageFilter.EMBOSS)
    return npImage_emboss

def equalizeFilter(npImage):
    return ImageOps.equalize(npImage)

def invertFilter(npImage):
    return ImageOps.invert(npImage)

def showImage(npImage):
    # print(np.max(npImage))
    npImage = np.uint8(npImage)
    cv2.imshow(‘Output’, npImage)

def prccessingPipeline(npImage, Pipeline):
    for filter in Pipeline:
        npImage = filter(npImage)
    return npImage


if __name__ == ‘__main__’:
    PipelineA = [embossFilter, equalizeFilter, invertFilter]
    PipelineB = [equalizeFilter, invertFilter]
    PipelineC = [embossFilter, equalizeFilter]

    Pipeline = PipelineA
    webcam = initializeWebCam()
    while True:
        videoFrame = getImage(webcam)
        videoFrame = prccessingPipeline(videoFrame, Pipeline)
        showImage(videoFrame)
        keypress = cv2.waitKey(1) & 0xFF
        if keypress == ord(‘q’):
            break
        elif keypress == ord(‘a’):
            Pipeline = PipelineA
        elif keypress == ord(‘b’):
            Pipeline = PipelineB
        elif keypress == ord(‘c’):
            Pipeline = PipelineC
    terminateWebCam(webcam)
    cv2.destroyAllWindows()
