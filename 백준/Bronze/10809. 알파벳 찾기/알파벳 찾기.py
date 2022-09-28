inStr = input()
alpha = [chr(i) for i in range(97, 123)]
answer = ''

for i in alpha:
    try:
        answer += str(inStr.index(i))
        answer += ' '
    except:
        answer += '-1 '
        
print(answer[:-1])