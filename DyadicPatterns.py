#!/usr/bin/python3

from sys import argv
from math import ceil, floor
import numpy as np
import cv2


def DyadicPattern(k, t):
    res = np.zeros([W, H])
    if k == 0:
        res[0][0] = 1
    else:
        n_res = DyadicPattern(k - 1, floor(t / 2))
        res = DyadicPattern(k - 1, floor(t / 2))

        for i in range(len(n_res)):
            for j in range(len(n_res)):
                n_res[(i + 2**(k-1)) % W][(j + ceil(t/2)) % H] = res[i][j]

        res = res + n_res

    return res


def main():
    k = int(input("Enter k: "))
    t = int(input("Enter t: "))
    if t > 2 ** k - 1:
        print("t must be less than 2^k")
        return

    global W
    global H
    
    W = 2 ** k
    H = 2 ** k

    if "-L" in argv or "-l" in argv or "--large" in argv:

        img_0 = np.zeros([W, H])
        img_0 = DyadicPattern(k, t)

        W = W * 8
        H = H * 8

        img = np.zeros([W, H])
        for i in range(len(img)):
            for j in range(len(img)):
                img[i][j] = img_0[i//8][j//8]
    else:
        img = np.zeros([W, H])
        img = DyadicPattern(k, t)

    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    for i in range(len(img)):
        for j in range(len(img)):
            img[i][j] = int(not(img[i][j]))

    img = 255 * img

    cv2.imwrite('./Pictures/DyadicPattern.png', img)    
    cv2.imshow(f"Dyadic Pattern for k = {k} and t = {t}", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

if __name__ == '__main__':
    main()