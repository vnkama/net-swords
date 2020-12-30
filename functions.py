import numpy as np


def calcDistancePoints2(coord1, coord2):
    return np.rint(np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2))

def calcDistancePoint1(coord):
    return np.rint(np.sqrt((coord[0])**2 + (coord[1])**2))