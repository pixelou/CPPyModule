#/usr/bin/env python

import sys

import cv2
import pyflipping
import numpy as np


def main():
    assert len(sys.argv) > 1, "Pass image file as argument."
   
    I = cv2.imread(sys.argv[-1])
    assert I is not None, "Failed to open image."
    
    cv2.namedWindow("cat", cv2.WINDOW_NORMAL)
    cv2.imshow("cat", I)
    cv2.waitKey(0)
    J = pyflipping.vertflip(I)
    cv2.imshow("cat", J)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    main()
