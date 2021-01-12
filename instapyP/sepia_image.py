import cv2
import numpy as np


def sepia_image(input_filename, output_filename=None):
    
    """
    Tar inn en numpy array av et bilde og en string med bildefilnavn eller path
    og lagrer bilde som fil til ønsket directory

    Args:
        param1 (input_filename,numpy Array):
        param2 (output_filename,str):

    returns:
        numpy arrayen av bildet
    """

    if output_filename != None:
        cv2.imwrite(output_filename,input_filename)

    return input_filename
