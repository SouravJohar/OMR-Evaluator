import numpy as np
import cv2
from FileReader import readKey
#loadedOMR = cv2.imread('sampleOMR.png')
#splitOne = loadedOMR[0:721, 0:500]
def evaluateBubble(loadedOMR,givenKey, currentQuestion, currentSplit, pt, w, h):

    chosenAnswer = ""
    numberOfAttempts = 0
    isAttempted = False

    bubbleRow = currentSplit[(pt[1] - h):pt[1] + 2*w + 5,pt[0]:(pt[0]+270)]
    t, bubbleRowThresh = cv2.threshold(bubbleRow, 200, 255, cv2.THRESH_BINARY_INV)
    circles = cv2.HoughCircles(bubbleRow, cv2.HOUGH_GRADIENT,1,20,param1=500,param2=10,minRadius=20,maxRadius=30)
    circles = np.uint16(np.around(circles))

    for i in circles[0,:]:
        bubbleDistance = i[0] - pt[0]
        #print i[0], pt[0], bubbleDistance
        whitePixels = 0
        #cv2.circle(bubbleRow,(i[0],i[1]),i[2],(0,255,0),2)

        for j in range(i[1] - 12, i[1] + 12):
            for k in range(i[0] - 12,i[0] + 12):
                if bubbleRowThresh[j,k] >200:
                    whitePixels+=1
        if whitePixels > 100 and ((bubbleDistance in range(0, 20)and currentQuestion < 11) or bubbleDistance in range(-95, -110, -1)and currentQuestion > 10):
             #print bubbleDistance

             x,y = i[0] + pt[0], i[1]+ pt[1] - h
             chosenAnswer += "A"
             numberOfAttempts+=1
        if whitePixels > 100 and ((bubbleDistance in range(55, 70)and currentQuestion < 11) or bubbleDistance in range(-38, -53, -1)and currentQuestion > 10):
             x,y = i[0] + pt[0], i[1]+ pt[1] - h
             chosenAnswer += "B"
             #print bubbleDistance
             numberOfAttempts+=1
             #x,y = i[0], i[1]
        if whitePixels > 100 and ((bubbleDistance in range(110, 130)and currentQuestion < 11) or bubbleDistance in range(5,20) and currentQuestion > 10):
             x,y = i[0] + pt[0], i[1]+ pt[1] - h
             chosenAnswer += "C"
             #print bubbleDistance       CAN REMOVE numberOfAttempts WITH LEN OF CHOSEN ANSWER!!!!!!!!!
             numberOfAttempts+=1

             #x,y = i[0], i[1]
        if whitePixels > 100 and ((bubbleDistance in range(170, 185)and currentQuestion < 11) or bubbleDistance in range(60,75) and currentQuestion > 10):
             x,y = i[0] + pt[0], i[1]+ pt[1] - h
             chosenAnswer += "D"
             #print bubbleDistance
             numberOfAttempts+=1
             #x,y = i[0], i[1]
        if numberOfAttempts == 0:
            #print "no" + str(bubbleDistance)
            pass

    currentScore, ret = keyMatch(currentQuestion,givenKey, numberOfAttempts, chosenAnswer)
    if currentScore == -1 and currentQuestion < 11:
           cv2.circle(loadedOMR,(x,y),i[2]-2,(0,0,255), 2)
           cv2.putText(loadedOMR,"-1",(x-10,y+4), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),1,cv2.LINE_AA)#CHANGE TO COLOR!!!!!
    if currentScore == 4 and  currentQuestion < 11:
           cv2.putText(loadedOMR,"+4",(x-10,y+4), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,255,0),1,cv2.LINE_AA)
           cv2.circle(loadedOMR,(x,y),i[2]-2,(0,255,0),2)
    if currentScore == -1 and currentQuestion > 10:
           cv2.putText(loadedOMR,"-1",(x-10+500,y+4), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),1,cv2.LINE_AA)
           cv2.circle(loadedOMR,(x+500,y),i[2]-2,(0,0,255),2) #CHANGE TO COLOR!!!!!
    if currentScore == 4 and  currentQuestion > 10:
           cv2.putText(loadedOMR,"+4",(x-10+500,y+4), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,255,0),1,cv2.LINE_AA)
           cv2.circle(loadedOMR,(x+500,y),i[2]-2,(0,255,0),2)

    #cv2.imshow("OMR Evaluator", loadedOMR)
    #cv2.imshow("OMR Evaluator", currentSplit)
    #time.sleep(1)
    #print currentQuestion, chosenAnswer, ret
    return currentScore


def keyMatch(currentQuestion,givenKey, numberOfAttempts, chosenAnswer):
    if numberOfAttempts > 1 or numberOfAttempts == 0:
        return 0, "Not attended" #key value goes here
    if chosenAnswer == givenKey[currentQuestion-1]:
        return 4, "Correct" #key value
    else:
        return -1, "Wrong" #keyValue
