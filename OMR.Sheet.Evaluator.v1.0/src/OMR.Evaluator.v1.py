import cv2
import numpy as np
import FileReader
from digitRecognizer import getNextDigit
from digitRecognizer import *
from bubbleEvaluator import evaluateBubble
from bubbleEvaluator import keyMatch
import os
import time

print "\t\t\t    OMR Sheet Evaluator"
givenKey = FileReader.readKey()
sheetLocation = raw_input(">Enter OMR sheet(s) location: ")
for sheet in os.listdir(sheetLocation):
    loadedOMR = cv2.imread(sheetLocation+"/"+ sheet)
    print givenKey
    finalScore = 0
    currentScore = 0

    splitOne = loadedOMR[0:721, 0:500]
    splitTwo = loadedOMR[0:721, 500:1026]
    splitOneGray = cv2.cvtColor(splitOne, cv2.COLOR_BGR2GRAY)
    splitTwoGray = cv2.cvtColor(splitTwo, cv2.COLOR_BGR2GRAY)

    threshold = 0.95
    currentSplit = splitOneGray
    isOne, pt, w, h = oneDetected(currentSplit, threshold)
    if isOne:
        currentQuestion = 1
        currentScore = evaluateBubble(loadedOMR, givenKey, currentQuestion, currentSplit, pt, w, h)
        finalScore += currentScore

    for count in range(1,10):
       if count > 10:
           currentSplit = splitTwoGray
       nextDigit, pt, w, h = getNextDigit(count, currentSplit, threshold)
       if nextDigit == count+1:
           currentQuestion = count+1
           currentScore = evaluateBubble(loadedOMR,givenKey, currentQuestion, currentSplit, pt, w, h)
           finalScore += currentScore
           #print finalScore

    currentSplit = splitTwoGray
    isEleven, pt, w, h = elevenDetected(currentSplit, threshold)

    if isEleven:
        currentQuestion = 11
        currentScore = evaluateBubble(loadedOMR,givenKey, currentQuestion, currentSplit, pt, w, h)
        finalScore += currentScore

    for count in range(11,20):
       nextDigit, pt, w, h = getNextDigit(count, currentSplit, threshold)
       if nextDigit == count+1:
           currentQuestion = count+1
           currentScore = evaluateBubble(loadedOMR,givenKey, currentQuestion, currentSplit, pt, w, h)
           finalScore += currentScore
    finalScore = (finalScore/80.0)*100
    cv2.putText(loadedOMR,str(finalScore) + "%",(50,60), cv2.FONT_HERSHEY_SIMPLEX, 2,(150,155,0),2,cv2.LINE_AA)
    #cv2.imshow("OMR Evaluator", loadedOMR)
    cv2.imwrite("./ApplicationData/Evaluated Sheets/ " + str(finalScore) + "% " +sheet[:len(sheet) -4] +  ".png", loadedOMR)
    #time.sleep(3)
    cv2.destroyAllWindows()
print "Sheet(s) evaluated"
time.sleep(3)
