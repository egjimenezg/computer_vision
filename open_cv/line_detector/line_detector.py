import cv2
import numpy as np

def slope(line):
    (x1, y1, x2, y2) = line
    return None if x2 - x1 == 0 else (y2 - y1) / (x2 - x1)

def main():
  image = cv2.imread("polygon.jpg")
  min_line_length=20
  gray_scale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  constant = 5
  binary_image = cv2.adaptiveThreshold(gray_scale_image ,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY + cv2.THRESH_BINARY_INV, 31, 5)
  lines = cv2.HoughLinesP(binary_image, 1, np.pi / 180, 30, minLineLength=min_line_length)
  lines = [line[0] for line in lines]
  diagonals = list(filter(lambda line: slope(line) is not None, lines))

  for (x1, y1, x2, y2) in diagonals:
    cv2.line(image, (x1, y1), (x2, y2), (235, 52, 82), 1)
  cv2.imwrite("diagonals.png", image)


if __name__ == "__main__":
    main()
