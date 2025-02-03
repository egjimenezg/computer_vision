import cv2
import numpy as np

def slope(line):
    (x1, y1, x2, y2) = line
    return None if x2 - x1 == 0 else y2 - y1 / x2 - x1

def main():
  image = cv2.imread("polygon.jpg")
  gray_scale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  edges = cv2.Canny(gray_scale_image, 0, 100)
  lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100)
  diagonals = list(filter(lambda line: slope(line[0]) is not None and slope(line[0]) > 0, lines))


if __name__ == "__main__":
    main()
