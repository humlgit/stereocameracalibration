import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('frame.jpg',0)
edges = cv.Canny(img,100,200)
edges1 = cv.Canny(img,0,100)
edges2 = cv.Canny(img,0,30)
plt.subplot(221),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(edges1,cmap = 'gray')
plt.title('Edge Image1'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(edges2,cmap = 'gray')
plt.title('Edge Image2'), plt.xticks([]), plt.yticks([])
plt.show()  