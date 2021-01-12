import cv2
import numpy as np
import time
from numba import njit


def numba_color2gray(image):

    """
    en numba implementasjon av transformasjon fra farge til gråtone bilde

    Args:
        param1 (image, numpy Array):

    returns:
        numpy arrayen av gråtone bildet
    """

    if (isinstance(image, str)):
        image = cv2.imread(image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #start = time.time()
    image = calculate(image)
    #end = time.time()
    #print(end - start,"seconds")
    return image

@njit
def calculate(image):

    """
    en hjelpemetode for og kunne bruke numba til å gjøre utregningen

    Args:
        param1 (image, numpy Array):

    returns:
        numpy arrayen av gråtone bildet
    """

    N = len(image)
    M = len(image[0])
    utbilde = np.zeros((N,M))
    for r in range(len(image)):
        for g in range(len(image[0])):
            utbilde[r][g] = image[r][g][0]*0.21+image[r][g][1]*0.72+image[r][g][2]*0.07
    return utbilde
