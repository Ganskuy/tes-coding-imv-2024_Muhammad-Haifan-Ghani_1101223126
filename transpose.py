#Orientasi gambar
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import cv2


plt.title("Dek Awas Ada Api")
plt.xlabel("X pixel scaling")
plt.ylabel("Y pixels scaling")
 
image = plt.imread("fire.jpg")
plt.imshow(image)
img_90=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
img_180=cv2.rotate(image,cv2.ROTATE_180)
img_270=cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)
img_flip=cv2.flip(image, 10)

fig = plt.figure(figsize=(20,20))

ax1 = fig.add_subplot(1,5,1)
ax1.set_title("ORI")
ax1.imshow(image)
ax2 = fig.add_subplot(1,5,2)
ax2.set_title("90CW")
ax2.imshow(img_90)
ax3 = fig.add_subplot(1,5,3)
ax3.set_title("180")
ax3.imshow(img_180)
ax4 = fig.add_subplot(1,5,4)
ax4.set_title("90CCW")
ax4.imshow(img_270)
ax5 = fig.add_subplot(1,5,5)
ax5.set_title("Flip Horizontal")
ax5.imshow(img_flip)