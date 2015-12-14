import urllib2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io

def main():
    image = io.imread("http://www.pythonchallenge.com/pc/def/oxygen.png")
    #print image.shape
    hint = []
    raw_hint = []

    for i in xrange(image.shape[0]):
        for j in xrange(image.shape[1]):
            r = image[i][j][0]
            g = image[i][j][1]
            b = image[i][j][2]
            if r == g == b:
                raw_hint.append(r)
    n = 0
    while (7*n < len(raw_hint)):
        hint.append(raw_hint[7*n])
        n = n+1

    #print "".join(map(chr, hint))
    #The list if from the previous hint
    nextlevel = [105, 110, 116, 101, 103, 114, 105, 116, 121]
    print "".join(map(chr, nextlevel))

if __name__ == "__main__":
    main()
