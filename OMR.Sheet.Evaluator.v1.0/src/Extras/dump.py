isTwo, pt, w, h = twoDetected(splitOneGray, threshold)
if isTwo:
    currentQuestion = 2
    finalScore += evaluateBubble(currentQuestion,splitOneGray, pt, w, h)

isThree, pt, w, h = threeDetected(splitOneGray, threshold)
if isThree:
    currentQuestion = 3
    finalScore += evaluateBubble(currentQuestion,splitOneGray, pt, w, h)

isFour, pt, w, h = fourDetected(splitOneGray, threshold)
if isTwo:
    currentQuestion = 4
    finalScore += evaluateBubble(currentQuestion,splitOneGray, pt, w, h)

isFive, pt, w, h = fiveDetected(splitOneGray, threshold)
if isFive:
    currentQuestion = 5
    finalScore += evaluateBubble(currentQuestion,splitOneGray, pt, w, h)

isSix, pt, w, h = sixDetected(splitOneGray, threshold)
if isSix:
    currentQuestion = 6
    finalScore += evaluateBubble(currentQuestion,splitOneGray, pt, w, h)

isSeven, pt, w, h = sevenDetected(splitOneGray, threshold)
if isSeven:
    currentQuestion = 7
    finalScore += evaluateBubble(currentQuestion,splitOneGray, pt, w, h)

isEight, pt, w, h = eightDetected(splitOneGray, threshold)
if isEight:
    currentQuestion = 8
    finalScore += evaluateBubble(currentQuestion,splitOneGray,pt, w, h)

isNine, pt, w, h = nineDetected(splitOneGray, threshold)
if isNine:
    currentQuestion = 9
    finalScore += evaluateBubble(currentQuestion,splitOneGray, pt, w, h)

isTen, pt, w, h = tenDetected(splitOneGray, threshold)
if isTen:
    currentQuestion = 10
    finalScore += evaluateBubble(currentQuestion,splitOneGray, pt, w, h)
