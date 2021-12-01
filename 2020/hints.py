from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt
from string import ascii_uppercase
import sys
import os

templates = [file for file in os.listdir('Templates') if file[0] == 'T']

image = cv2.imread('Templates\hint1.png')
original = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
canny = cv2.Canny(blurred, 120, 255, 1)
kernel = np.ones((2,2),np.uint8)
dilate = cv2.dilate(canny, kernel, iterations=1)

# Find contours
cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

# Iterate through contours and sort them
box = []
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    if w > 12 and h > 12:
        box.append((y//15, x//10, x, y, w, h))
box.sort()

# Iterate through sorted contours and assign a letter if known
hint = []
for _, _, x, y, w, h in box:
    char = '.'
    cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
    ROI = original[y:y+h, x:x+w]

    # for template_file in templates:
    #     template = cv2.imread('Templates/' + template_file, 0)
    #     wt, ht = template.shape[::]
    #
    #     res = cv2.matchTemplate(ROI, template, cv2.TM_CCOEFF_NORMED)
    #     threshold = 0.9
    #     loc = np.where(res >= threshold)
    #     print(loc)
    #     sys.exit()

cv2.imshow('canny', canny)
cv2.imshow('image', image)
cv2.waitKey(0)

sys.exit()

img_rgb = cv2.imread('Templates/hint1.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# color = [(0,0,255), (0,255,0), (255,0,0), (0,255,255)]

count = 0
loc_hint = []
for letter in ascii_uppercase:
    template = cv2.imread('Templates/template' + letter + '.png', 0)
    w, h = template.shape[::]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9605
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        count += 1
        loc_hint.append((pt[1]//10, pt[0]//10, letter))
    #     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), color[i-1], 2)

loc_hint.sort()
x = []
for pt in loc_hint:
    x.append(str(pt[2]))
x = ''.join(x)
print(x)
plt.imshow(img_rgb)
plt.show

