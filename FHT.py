#!/usr/bin/python3

from time import sleep
import numpy as np
from sys import argv
import cv2

W = 2 ** 9
H = 2 ** 9
dim = (W, H)
Pixel_Distance = 10000
Threshold = 15000

def calc_sums(img, xmin, xmax):
    res = np.zeros([W, xmax-xmin])
    if xmax - xmin == 1:
        res[:, 0] = img[:, xmin]
    else:
        mid = (xmin + xmax) // 2
        ans1 = calc_sums(img, xmin, mid)
        ans2 = calc_sums(img, mid, xmax)
        for x in range(W):
            for shift in range(xmax - xmin):
                if (x + shift // 2 + shift % 2) < W:
                    res[x, shift] = ans1[x, shift // 2] + ans2[(x + shift // 2 + shift % 2), shift // 2]
    return res

def MaxValid(Maxima, n):
    for k in range(n):
        x_n = Maxima[n][1]
        x_p = Maxima[k][1]
        y_n = Maxima[n][0]
        y_p = Maxima[k][0]
        if (x_n - x_p) ** 2 + (y_n - y_p) ** 2 < Pixel_Distance:
            return False
    return True

def main():
    path = argv[1]

    img1  = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img1  = cv2.resize(img1, dim)

    img2  = cv2.rotate(img1, cv2.cv2.ROTATE_90_CLOCKWISE)
    
    img3  = cv2.flip(img2, 1)

    img4  = cv2.rotate(img3, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

    orig = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    orig = cv2.resize(img1, dim)

    res1 = calc_sums(img1, 0, W)
    Maxima = []
    for i in range(len(res1)):
        for j in range(len(res1)):
            if res1[i][j] > Threshold:
                Maxima.append((i, j, res1[i][j]))           

    Maxima.sort(key=lambda Max: Max[2], reverse=True)
    
    for n in range(1000):
        if n >= len(Maxima):
            break
        if n > 0:
            if not MaxValid(Maxima, n):
                continue

        (y, x, Max) = Maxima[n]
        img1 = cv2.line(img1, (0, y), (W, x + y), (255, 0, 0), 2)
        res1 = cv2.circle(res1, (x, y), radius=5, color=(255, 0, 0), thickness=-1)


    img1 = cv2.rotate(img1, cv2.cv2.ROTATE_90_CLOCKWISE)
    res2 = calc_sums(img2, 0, W)
    Maxima = []
    for i in range(len(res2)):
        for j in range(len(res2)):
            if res2[i][j] > Threshold:
                Maxima.append((i, j, res2[i][j]))
                
    Maxima.sort(key=lambda Max: Max[2], reverse=True)
    
    for n in range(1000):
        if n >= len(Maxima):
            break
        if n > 0:
            if not MaxValid(Maxima, n):
                continue

        (y, x, Max) = Maxima[n]
        img1 = cv2.line(img1, (0, y), (W, x + y), (255, 0, 0), 2)
        res2 = cv2.circle(res2, (x, y), radius=5, color=(255, 0, 0), thickness=-1)


    img1 = cv2.flip(img1, 1)
    res3 = calc_sums(img3, 0, W)
    Maxima = []
    for i in range(len(res3)):
        for j in range(len(res3)):
            if res3[i][j] > Threshold:
                Maxima.append((i, j, res3[i][j]))
                
    Maxima.sort(key=lambda Max: Max[2], reverse=True)
    
    for n in range(1000):
        if n >= len(Maxima):
            break
        if n > 0:
            if not MaxValid(Maxima, n):
                continue

        (y, x, Max) = Maxima[n]
        img1 = cv2.line(img1, (0, y), (W, x + y), (255, 0, 0), 2)
        res3 = cv2.circle(res3, (x, y), radius=5, color=(255, 0, 0), thickness=-1)


    img1 = cv2.rotate(img1, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
    res4 = calc_sums(img4, 0, W)
    Maxima = []
    for i in range(len(res4)):
        for j in range(len(res4)):
            if res4[i][j] > Threshold:
                Maxima.append((i, j, res4[i][j]))
                
    Maxima.sort(key=lambda Max: Max[2], reverse=True)

    for n in range(1000):
        if n >= len(Maxima):
            break
        if n > 0:
            if not MaxValid(Maxima, n):
                continue

        (y, x, Max) = Maxima[n]
        img1 = cv2.line(img1, (0, y), (W, x + y), (255, 0, 0), 2)
        res4 = cv2.circle(res4, (x, y), radius=5, color=(255, 0, 0), thickness=-1)


    img1 = cv2.flip(img1, 0)

    # Multiply by 4 to see whole picture easily
    res1 = res1 / res1.max() * 4
    cv2.imshow("Fast Hough Image", res1)

    cv2.imshow("Detected_" + path, img1)
    cv2.imshow("Original", orig)
    cv2.waitKey(0)
    cv2.destroyAllWindows()   

if __name__ == '__main__':
    main()