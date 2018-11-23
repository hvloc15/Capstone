import numpy
import cv2


def read_opencv_image(inmemory_image):
    image_bytestream = inmemory_image.file.read()
    return cv2.imdecode(numpy.fromstring(image_bytestream, numpy.uint8), cv2.IMREAD_UNCHANGED)
