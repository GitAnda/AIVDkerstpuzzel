from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

img_rgb = cv2.imread('subscript_page.jpeg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
color = [(0,0,255), (0,255,0), (255,0,0), (0,255,255)]

count = 0
p = []
for i in range(1,5):
    template = cv2.imread('template'+ str(i) +'.png',0)
    w, h = template.shape[::]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.9605
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        count += 1
        p.append((pt[1]//10, pt[0]//10, i))
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), color[i-1], 2)

p = sorted(p)
x = []
for pt in p:
    x.append(str(pt[2]))
x = ''.join(x)
x = x.replace('4', '|').replace('3', ' ').replace('1', '.').replace('2', '-')
print(x)
cv2.imwrite('res.png',img_rgb)

# WIE SPEELDE HET TITELKARAKTER IN DE PERSOONLIJKE GESCHIEDENIS DIE DIT JAAR IN NEDERLAND UITGEBRACHT WERD?