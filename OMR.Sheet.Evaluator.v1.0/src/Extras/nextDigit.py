def getNextDigit(currentQuestion, splitOneGray, threshold):
    
    if currentQuestion == 1:
        isTwo, pt, w, h = twoDetected(splitOneGray, threshold)
        if isTwo:
            return 2, pt, w, h
    if currentQuestion == 2:
        isThree, pt, w, h = threeDetected(splitOneGray, threshold)
        if isThree:
            return 3, pt, w, h
    if currentQuestion == 3:
        isFour, pt, w, h = fourDetected(splitOneGray, threshold)
        if isFour:
            return 4, pt, w, h
    if currentQuestion == 4:
        isFive, pt, w, h = fiveDetected(splitOneGray, threshold)
        if isFive:
            return 5, pt, w, h
    if currentQuestion == 5:
        iSix, pt, w, h = sixDetected(splitOneGray, threshold)
        if isSix:
            return 6, pt, w, h
    if currentQuestion == 6:
        isSeven, pt, w, h = sevenDetected(splitOneGray, threshold)
        if isSeven:
            return 7, pt, w, h
    if currentQuestion == 7:
        isEight, pt, w, h = eightDetected(splitOneGray, threshold)
        if isEight:
            return 8, pt, w, h
    if currentQuestion == 8:
        isNine, pt, w, h = nineDetected(splitOneGray, threshold)
        if isNine:
            return 9, pt, w, h
    if currentQuestion == 9:
        isTen, pt, w, h = tenDetected(splitOneGray, threshold)
        if isTen:
            return 10, pt, w, h
