import cv2
import numpy as np
import time


def python_color2gray(image):

    """
    en enkel python implementasjon av transformasjon av farge til gråtone bilde

    Args:
        param1 (image, numpy Array):

    returns:
        numpy arrayen av gråtone bildet
    """

    if (isinstance(image, str)):
        image = cv2.imread(image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    N = len(image)
    M = len(image[0])
    utbilde = np.zeros((N,M))
    for r in range(len(image)):
        for g in range(len(image[0])):
            utbilde[r][g] = image[r][g][0]*0.21+image[r][g][1]*0.72+image[r][g][2]*0.07
    return utbilde



# start = time.time()
# utbilde = python_color2gray("rain.jpg")
# end = time.time()
# print(end - start,"seconds")
#
#
# utbilde = utbilde.astype("uint8")
# cv2.imshow('image',utbilde)
# cv2.waitKey(0)
# cv2.imwrite("raingrayscale.jpeg",utbilde)
