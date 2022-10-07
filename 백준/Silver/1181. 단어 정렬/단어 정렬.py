num = int(input())
word = {}
for i in range(num):
    inputW = input()
    try:
        word[len(inputW)].append(inputW)
    except:
        word[len(inputW)] = [inputW]
word = sorted(word.items())
for i,j in word:
    j = list(set(j))
    j.sort()
    for k in j:
        print(k)