def readKey():
    keyLocation = raw_input(">Location of key: ")
    givenKey = open(keyLocation, 'r')
    answerKey = givenKey.read()
    correct, incorrect, other = int(answerKey[0]), int(answerKey[2:4]), int(answerKey[5])
    answers = []
    answers.append(answerKey[answerKey.find("-1-") + 3])
    answers.append(answerKey[answerKey.find("-2-") + 3])
    answers.append(answerKey[answerKey.find("-3-") + 3])
    answers.append(answerKey[answerKey.find("-4-") + 3])
    answers.append(answerKey[answerKey.find("-5-") + 3])
    answers.append(answerKey[answerKey.find("-6-") + 3])
    answers.append(answerKey[answerKey.find("-7-") + 3])
    answers.append(answerKey[answerKey.find("-8-") + 3])
    answers.append(answerKey[answerKey.find("-9-") + 3])
    answers.append(answerKey[answerKey.find("-10-") + 4])
    answers.append(answerKey[answerKey.find("-11-") + 4])
    answers.append(answerKey[answerKey.find("-12-") + 4])
    answers.append(answerKey[answerKey.find("-13-") + 4])
    answers.append(answerKey[answerKey.find("-14-") + 4])
    answers.append(answerKey[answerKey.find("-15-") + 4])
    answers.append(answerKey[answerKey.find("-16-") + 4])
    answers.append(answerKey[answerKey.find("-17-") + 4])
    answers.append(answerKey[answerKey.find("-18-") + 4])
    answers.append(answerKey[answerKey.find("-19-") + 4])
    answers.append(answerKey[answerKey.find("-20-") + 4])
    return answers
    
    
