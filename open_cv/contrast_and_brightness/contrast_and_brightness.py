import cv2

def main():
  image = cv2.imread("mountains.jpg")
  # Increase brightness
  brighter_image = cv2.convertScaleAbs(image, beta=70)
  cv2.imwrite("brighter_image.jpg", brighter_image)
  # Increase contrast
  image = cv2.convertScaleAbs(image, alpha=2)
  cv2.imwrite("higher_contrast_image.jpg", image)

if __name__ == "__main__":
  main()
