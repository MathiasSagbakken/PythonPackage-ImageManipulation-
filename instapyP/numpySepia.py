import cv2
import numpy as np
import time


def numpy_color2sepia(image):

    """
    numpy implementasjon som transfomerer et farge bilde med et sepia filter

    Args:
        param1 (image,numpy Array):

    returns:
        numpy arrayen av sepia bildet
    """

    if (isinstance(image, str)):
        image = cv2.imread(image)

    filter = np.array([[.393, .769, .189],
                         [.349, .686, .168],
                         [.272, .534, .131]])

    N = len(image)
    M = len(image[0])
    utbilde = np.zeros((N,M,3))

    utbilde = image.dot(filter.T)
    utbilde[utbilde>255] = 255

    utbilde[...,[0,2]] = utbilde[...,[2,0]]  #cv2cvtcolor konvertering fungerer ikke så måtte lage denne erstatningen


    return utbilde
