import numpy as np
from instapyP.python_color2gray import python_color2gray
from instapyP.numpy_color2gray import numpy_color2gray
from instapyP.numba_color2gray import numba_color2gray
from instapyP.pythonSepia import python_color2sepia
from instapyP.numpySepia import numpy_color2sepia
from instapyP.numbaSepia import numba_color2sepia

def test_gray():

    """
    en test metode for alle gråtone bilder som spesifisert i oppgaven

    Args:
        -

    returns:
        -
    """

    randArr = np.random.randint(0, 255, size=(250, 250, 3))
    assert len(python_color2gray(randArr).shape) == 2
    assert len(numpy_color2gray(randArr).shape) == 2
    assert len(numba_color2gray(randArr).shape) == 2
    x = np.random.randint(0,250)
    y = np.random.randint(0,250)
    assert python_color2gray(randArr)[x][y] == randArr[x][y][0]*0.21+randArr[x][y][1]*0.72+randArr[x][y][2]*0.07
    assert numpy_color2gray(randArr)[x][y] == randArr[x][y][0]*0.21+randArr[x][y][1]*0.72+randArr[x][y][2]*0.07
    assert numba_color2gray(randArr)[x][y] == randArr[x][y][0]*0.21+randArr[x][y][1]*0.72+randArr[x][y][2]*0.07


test_gray()


def test_sepia():

    """
    en test metode for alle sepia bilder som spesifisert i oppgaven

    Args:
        -

    returns:
        -
    """

    randArr = np.random.randint(0, 255, size=(250, 250, 3))
    x = np.random.randint(0,250)
    y = np.random.randint(0,250)
    assert python_color2sepia(randArr)[x][y][2] == randArr[x][y][0]*0.393+randArr[x][y][1]*0.769+randArr[x][y][2]*0.189
    assert python_color2sepia(randArr)[x][y][1] == randArr[x][y][0]*0.349+randArr[x][y][1]*0.686+randArr[x][y][2]*0.168
    assert python_color2sepia(randArr)[x][y][0] == randArr[x][y][0]*0.272+randArr[x][y][1]*0.534+randArr[x][y][2]*0.131

    assert numpy_color2sepia(randArr)[x][y][2] == randArr[x][y][0]*0.393+randArr[x][y][1]*0.769+randArr[x][y][2]*0.189
    assert numpy_color2sepia(randArr)[x][y][1] == randArr[x][y][0]*0.349+randArr[x][y][1]*0.686+randArr[x][y][2]*0.168
    assert numpy_color2sepia(randArr)[x][y][0] == randArr[x][y][0]*0.272+randArr[x][y][1]*0.534+randArr[x][y][2]*0.131

    assert numba_color2sepia(randArr)[x][y][2] == randArr[x][y][0]*0.393+randArr[x][y][1]*0.769+randArr[x][y][2]*0.189
    assert numba_color2sepia(randArr)[x][y][1] == randArr[x][y][0]*0.349+randArr[x][y][1]*0.686+randArr[x][y][2]*0.168
    assert numba_color2sepia(randArr)[x][y][0] == randArr[x][y][0]*0.272+randArr[x][y][1]*0.534+randArr[x][y][2]*0.131


test_sepia()
