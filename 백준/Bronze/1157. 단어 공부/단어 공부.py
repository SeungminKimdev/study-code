inStr = input()
count = {}

for i in inStr:
    try:
        count[i.upper()] += 1
    except:
        count[i.upper()] = 1
        
sortedCount = sorted(count.items(), key = lambda item: item[1], reverse=True)
if len(sortedCount) != 1 and sortedCount[0][1] == sortedCount[1][1]:
    print('?')
else:
    print(sortedCount[0][0])