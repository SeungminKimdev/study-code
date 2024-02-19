import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int,input().split()))
maxArray = array
minArray = array
for i in range(1,n):
    array = list(map(int,input().split()))
    temp = [0,0,0]
    temp[0] = array[0] + max(maxArray[0],maxArray[1])
    temp[1] = array[1] + max(maxArray[1],max(maxArray[2],maxArray[0]))
    temp[2] = array[2] + max(maxArray[1],maxArray[2])
    maxArray = temp
    temp = [0,0,0]
    temp[0] = array[0] + min(minArray[0],minArray[1])
    temp[1] = array[1] + min(minArray[1],min(minArray[2],minArray[0]))
    temp[2] = array[2] + min(minArray[1],minArray[2])
    minArray = temp
print('{} {}'.format(max(maxArray),min(minArray)))