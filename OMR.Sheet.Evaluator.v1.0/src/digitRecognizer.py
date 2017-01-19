import numpy as np
import cv2

def oneDetected(currentSplit, threshold):
    digit = cv2.imread('./ApplicationData/Digits/digitOne.png',0)
    w, h = digit.shape[::-1]
    digitDetected = cv2.matchTemplate(currentSplit,digit,cv2.TM_CCOEFF_NORMED)
    loc = np.where( digitDetected >= threshold)
    for pt in zip(*loc[::-1]):
        if pt[0] < 500:
            return True, pt, w, h

def twoDetected(currentSplit, threshold):
    digit = cv2.imread('./ApplicationData/Digits/digitTwo.png',0)
    w, h = digit.shape[::-1]
    digitDetected = cv2.matchTemplate(currentSplit,digit,cv2.TM_CCOEFF_NORMED)
    loc = np.where( digitDetected >= threshold)
    for pt in zip(*loc[::-1]):
        return True, pt, w, h

def threeDetected(currentSplit, threshold):
    digit = cv2.imread('./ApplicationData/Digits/digitThree.png',0)
    w, h = digit.shape[::-1]
    digitDetected = cv2.matchTemplate(currentSplit,digit,cv2.TM_CCOEFF_NORMED)
    loc = np.where( digitDetected >= threshold)
    for pt in zip(*loc[::-1]):
        return True, pt, w, h

def fourDetected(currentSplit, threshold):
    digit = cv2.imread('./ApplicationData/Digits/digitFour.png',0)
    w, h = digit.shape[::-1]
    digitDetected = cv2.matchTemplate(currentSplit,digit,cv2.TM_CCOEFF_NORMED)
    loc = np.where( digitDetected >= threshold)
    for pt in zip(*loc[::-1]):
        return True, pt, w, h

def fiveDetected(currentSplit, threshold):
    digit = cv2.imread('./ApplicationData/Digits/digitFive.png',0)
    w, h = digit.shape[::-1]
    digitDetected = cv2.matchTemplate(currentSplit,digit,cv2.TM_CCOEFF_NORMED)
    loc = np.where( digitDetected >= threshold)
    for pt in zip(*loc[::-1]):
        return True, pt, w, h

def sixDetected(currentSplit, threshold):
    digit = cv2.imread('./ApplicationData/Digits/digitSix.png',0)
    w, h = digit.shape[::-1]
    digitDetected = cv2.matchTemplate(currentSplit,digit,cv2.TM_CCOEFF_NORMED)
    loc = np.where( digitDetected >= threshold)
    for pt in zip(*loc[::-1]):
        return True, pt, w, h

def sevenDetected(currentSplit, threshold):
    digit = cv2.imread('./ApplicationData/Digits/digitSeven.png',0)
    w, h = digit.shape[::-1]
    digitDetected = cv2.matchTemplate(currentSplit,digit,cv2.TM_CCOEFF_NORMED)
    loc = np.where( digitDetected >= threshold)
    for pt in zip(*loc[::-1]):
        return True, pt, w, h

def eightDetected(currentSplit, threshold):
    digit = cv2.imread('./ApplicationData/Digits/digitEight.png',0)
    w, h = digit.shape[::-1]
    digitDetected = cv2.matchTemplate(currentSplit,digit,cv2.TM_CCOEFF_NORMED)
    loc = np.where( digitDetected >= threshold)
    for pt in zip(*loc[::-1]):
        return True, pt, w, h

def nineDetected(currentSplit, threshold):
    digit = cv2.imread('./ApplicationData/Digits/digitNine.png',0)
    w, h = digit.shape[::-1]
    digitDetected = cv2.matchTemplate(currentSplit,digit,cv2.TM_CCOEFF_NORMED)
    loc = np.where( digitDetected >= threshold)
    for pt in zip(*loc[::-1]):
        return True, pt, w, h

def tenDetected(currentSplit, threshold):
    digit = cv2.imread('./ApplicationData/Digits/numberTen.png',0)
    w, h = digit.shape[::-1]
    digitDetected = cv2.matchTemplate(currentSplit,digit,cv2.TM_CCOEFF_NORMED)
    loc = np.where( digitDetected >= threshold)
    for pt in zip(*loc[::-1]):
        return True, pt, w, h

def elevenDetected(currentSplit, threshold):
    digit = cv2.imread('./ApplicationData/Digits/numberEleven.png',0)
    w, h = digit.shape[::-1]
    digitDetected = cv2.matchTemplate(currentSplit,digit,cv2.TM_CCOEFF_NORMED)
    loc = np.where( digitDetected >= threshold)
    for pt in zip(*loc[::-1]):
        return True, pt, w, h

def twelveDetected(currentSplit, threshold):
    digit = cv2.imread('./ApplicationData/Digits/numberTwelve.png',0)
    w, h = digit.shape[::-1]
    digitDetected = cv2.matchTemplate(currentSplit,digit,cv2.TM_CCOEFF_NORMED)
    loc = np.where( digitDetected >= threshold)
    for pt in zip(*loc[::-1]):
        return True, pt, w, h

def thirteenDetected(currentSplit, threshold):
    digit = cv2.imread('./ApplicationData/Digits/numberThirteen.png',0)
    w, h = digit.shape[::-1]
    digitDetected = cv2.matchTemplate(currentSplit,digit,cv2.TM_CCOEFF_NORMED)
    loc = np.where( digitDetected >= threshold)
    for pt in zip(*loc[::-1]):
        return True, pt, w, h

def fourteenDetected(currentSplit, threshold):
    digit = cv2.imread('./ApplicationData/Digits/numberFourteen.png',0)
    w, h = digit.shape[::-1]
    digitDetected = cv2.matchTemplate(currentSplit,digit,cv2.TM_CCOEFF_NORMED)
    loc = np.where( digitDetected >= threshold)
    for pt in zip(*loc[::-1]):
        return True, pt, w, h

def fifteenDetected(currentSplit, threshold):
    digit = cv2.imread('./ApplicationData/Digits/numberFifteen.png',0)
    w, h = digit.shape[::-1]
    digitDetected = cv2.matchTemplate(currentSplit,digit,cv2.TM_CCOEFF_NORMED)
    loc = np.where( digitDetected >= threshold)
    for pt in zip(*loc[::-1]):
        return True, pt, w, h

def sixteenDetected(currentSplit, threshold):
    digit = cv2.imread('./ApplicationData/Digits/numberSixteen.png',0)
    w, h = digit.shape[::-1]
    digitDetected = cv2.matchTemplate(currentSplit,digit,cv2.TM_CCOEFF_NORMED)
    loc = np.where( digitDetected >= threshold)
    for pt in zip(*loc[::-1]):
        return True, pt, w, h

def seventeenDetected(currentSplit, threshold):
    digit = cv2.imread('./ApplicationData/Digits/numberSeventeen.png',0)
    w, h = digit.shape[::-1]
    digitDetected = cv2.matchTemplate(currentSplit,digit,cv2.TM_CCOEFF_NORMED)
    loc = np.where( digitDetected >= threshold)
    for pt in zip(*loc[::-1]):
        return True, pt, w, h

def eighteenDetected(currentSplit, threshold):
    digit = cv2.imread('./ApplicationData/Digits/numberEighteen.png',0)
    w, h = digit.shape[::-1]
    digitDetected = cv2.matchTemplate(currentSplit,digit,cv2.TM_CCOEFF_NORMED)
    loc = np.where( digitDetected >= threshold)
    for pt in zip(*loc[::-1]):
        return True, pt, w, h

def nineteenDetected(currentSplit, threshold):
    digit = cv2.imread('./ApplicationData/Digits/numberNineteen.png',0)
    w, h = digit.shape[::-1]
    digitDetected = cv2.matchTemplate(currentSplit,digit,cv2.TM_CCOEFF_NORMED)
    loc = np.where( digitDetected >= threshold)
    for pt in zip(*loc[::-1]):
        return True, pt, w, h

def twentyDetected(currentSplit, threshold):
    digit = cv2.imread('./ApplicationData/Digits/numberTwenty.png',0)
    w, h = digit.shape[::-1]
    digitDetected = cv2.matchTemplate(currentSplit,digit,cv2.TM_CCOEFF_NORMED)
    loc = np.where( digitDetected >= threshold)
    for pt in zip(*loc[::-1]):
        return True, pt, w, h

def getNextDigit(currentQuestion, currentSplit, threshold):

    if currentQuestion == 1:
        isTwo, pt, w, h = twoDetected(currentSplit, threshold)
        if isTwo:
            return 2, pt, w, h
    if currentQuestion == 2:
        isThree, pt, w, h = threeDetected(currentSplit, threshold)
        if isThree:
            return 3, pt, w, h
    if currentQuestion == 3:
        isFour, pt, w, h = fourDetected(currentSplit, threshold)
        if isFour:
            return 4, pt, w, h
    if currentQuestion == 4:
        isFive, pt, w, h = fiveDetected(currentSplit, threshold)
        if isFive:
            return 5, pt, w, h
    if currentQuestion == 5:
        isSix, pt, w, h = sixDetected(currentSplit, threshold)
        if isSix:
            return 6, pt, w, h
    if currentQuestion == 6:
        isSeven, pt, w, h = sevenDetected(currentSplit, threshold)
        if isSeven:
            return 7, pt, w, h
    if currentQuestion == 7:
        isEight, pt, w, h = eightDetected(currentSplit, threshold)
        if isEight:
            return 8, pt, w, h
    if currentQuestion == 8:
        isNine, pt, w, h = nineDetected(currentSplit, threshold)
        if isNine:
            return 9, pt, w, h
    if currentQuestion == 9:
        isTen, pt, w, h = tenDetected(currentSplit, threshold)
        if isTen:
            return 10, pt, w, h
    if currentQuestion == 10:
        isEleven, pt, w, h = elevenDetected(currentSplit, threshold)
        if isEleven:
            return 11, pt, w, h
    if currentQuestion == 11:
        isTwelve, pt, w, h = twelveDetected(currentSplit, threshold)
        if isTwelve:
            return 12, pt, w, h
    if currentQuestion == 12:
        isThirteen, pt, w, h = thirteenDetected(currentSplit, threshold)
        if isThirteen:
            return 13, pt, w, h
    if currentQuestion == 13:
        isFourteen, pt, w, h = fourteenDetected(currentSplit, threshold)
        if isFourteen:
            return 14, pt, w, h
    if currentQuestion == 14:
        isFifteen, pt, w, h = fifteenDetected(currentSplit, threshold)
        if isFifteen:
            return 15, pt, w, h
    if currentQuestion == 15:
        isSixteen, pt, w, h = sixteenDetected(currentSplit, threshold)
        if isSixteen:
            return 16, pt, w, h
    if currentQuestion == 16:
        isSeventeen, pt, w, h = seventeenDetected(currentSplit, threshold)
        if isSeventeen:
            return 17, pt, w, h
    if currentQuestion == 17:
        isEighteen, pt, w, h = eighteenDetected(currentSplit, threshold)
        if isEighteen:
            return 18, pt, w, h
    if currentQuestion == 18:
        isNineteen, pt, w, h = nineteenDetected(currentSplit, threshold)
        if isNineteen:
            return 19, pt, w, h
    if currentQuestion == 19:
        isTwenty, pt, w, h = twentyDetected(currentSplit, threshold)
        if isTwenty:
            return 20, pt, w, h
