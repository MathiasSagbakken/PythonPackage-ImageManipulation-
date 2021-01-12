import cv2
import numpy as np
import time
from numba import njit


def numba_color2sepia(image):
    if (isinstance(image, str)):
        image = cv2.imread(image)
    #start = time.time()
    utbilde = calculate(image)
    #end = time.time()
    #print(end - start,"seconds")
    return utbilde

@njit
def calculate(image):
    N = len(image)
    M = len(image[0])
    utbilde = np.zeros((N,M,3))
    for r in range(len(image)):
        for g in range(len(image[0])):
            utbilde[r][g][2] = image[r][g][0]*0.393+image[r][g][1]*0.769+image[r][g][2]*0.189
            if (utbilde[r][g][2] > 255):
                utbilde[r][g][2] = 255
            utbilde[r][g][1] = image[r][g][0]*0.349+image[r][g][1]*0.686+image[r][g][2]*0.168
            if (utbilde[r][g][1] > 255):
                utbilde[r][g][1] = 255
            utbilde[r][g][0] = image[r][g][0]*0.272+image[r][g][1]*0.534+image[r][g][2]*0.131
            if (utbilde[r][g][0] > 255):
                utbilde[r][g][0] = 255
    return utbilde



# image = cv2.imread("rain.jpg")
# utbilde = numba_color2sepia(image)
#
#
# utbilde = utbilde.astype("uint8")
# cv2.imshow('image',utbilde)
# cv2.waitKey(0)
# cv2.imwrite("rainsepia.jpeg",utbilde)
