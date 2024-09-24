inputString = input().rstrip()

while inputString != 'end':
    vowelsCount = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    beforeWord = ''
    vowelsContinue = 0
    consonantContinue = 0
    check = True
    for i in inputString:
        if i in vowels: # 모음
            consonantContinue = 0
            vowelsCount += 1
            vowelsContinue += 1
            if vowelsContinue == 3:
                check = False
                break
            if beforeWord == i:
                if i == 'e' or i == 'o':
                    pass
                else:
                    check = False
                    break
        else: # 자음
            vowelsContinue = 0
            consonantContinue += 1
            if consonantContinue == 3:
                check = False
                break
            if beforeWord == i:
                check = False
                break
        beforeWord = i
        
    if vowelsCount < 1:
        check = False
    
    if check:
        print(f'<{inputString}> is acceptable.')
    else:
        print(f'<{inputString}> is not acceptable.')
    
    inputString = input().rstrip()