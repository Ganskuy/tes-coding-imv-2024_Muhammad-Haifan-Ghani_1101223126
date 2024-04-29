import cv2

# Read the original image
image = cv2.imread('ayon.jpeg')

# Convert the image to grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert the image to black and white
bnw_image = cv2.threshold(grayscale_image, 127, 255, cv2.THRESH_BINARY)[1]

# Save the grayscale image
cv2.imwrite('ayon_grayscale.jpeg', grayscale_image)

# Save the black and white image
cv2.imwrite('ayon_bnw.jpeg', bnw_image)
