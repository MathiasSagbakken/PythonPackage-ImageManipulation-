import cv2
import numpy as np
import time


def numpy_color2gray(image):

    """
    en numpy implementasjon av transformasjon fra farge til gråtone bilde

    Args:
        param1 (image, numpy Array):

    returns:
        numpy arrayen av gråtone bildet
    """

    if (isinstance(image, str)):
        image = cv2.imread(image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return np.dot(image[...,:3], [0.21, 0.72, 0.07])
