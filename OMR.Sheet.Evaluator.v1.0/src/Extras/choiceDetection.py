import numpy as np
import cv2

loadedOMR = cv2.imread("sampleOMR.png")
splitOne = loadedOMR[0:721, 0:500]
splitOneGray = cv2.cvtColor(splitOne, cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(splitOneGray, 200, 255, cv2.THRESH_BINARY_INV)
circles = cv2.HoughCircles(splitOneGray, cv2.HOUGH_GRADIENT,1,20,param1=50,param2=10,minRadius=20,maxRadius=30)

circles = np.uint16(np.around(circles))
control = 0
for i in circles[0,:]:
    count = 0
    cv2.circle(splitOne,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.rectangle(splitOne, (i[0] - 12, i[1] - 12), (i[0] + 12, i[1] + 12), (255,0,0), 1)
    for j in range(i[0] - 12, i[0] + 13):
        for k in range(i[1] - 12,i[1] + 13):
            print threshold[j,k]
    if control == 0:
        break
            
    

cv2.imshow("lol", splitOne)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()

