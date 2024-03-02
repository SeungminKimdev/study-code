def solution(s):
    answer = ""
    length = len(s)
    i = 0
    numDict = {"ze":0,"on":1,"tw":2,"th":3,"fo":4,"fi":5,"si":6,"se":7,
              "ei":8,"ni":9}
    wordLength = {0:4,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4}
    while i < length:
        if ord(s[i]) >= 97:
            transNum = numDict[s[i:i+2]]
            answer += str(transNum)
            i += wordLength[transNum]
        else:
            answer += s[i]
            i += 1
    return int(answer)