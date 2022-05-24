#!/usr/bin/python3

from sys import argv
import numpy as np
import cv2

def main():
    path = argv[1]
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    res = cv2.imread(path, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 50, 200)
    # Detect points that form a line

    lines = cv2.HoughLines(edges, 1, np.pi/180, 250)
    if lines is not None:
        for i in range(len(lines)):
            for rho,theta in lines[i]:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * (a))
                cv2.line(res,(x1, y1),(x2, y2),(0, 0, 255), 2)

    cv2.imshow("Detected_" + path, res)
    cv2.imshow("Original", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

if __name__ == '__main__':
    main()