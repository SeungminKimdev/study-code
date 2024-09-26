n = int(input())
switchs = list(input().split())
students = int(input())
for i in range(students):
    sex, num = map(int, input().split())
    if sex == 1:
        for j in range(num-1, n, num):
            if switchs[j] == '0':
                switchs[j] = '1'
            else:
                switchs[j] = '0'
    else:
        num -= 1
        for j in range(1, n):
            if num-j < 0 or num+j >= n or switchs[num-j] != switchs[num+j]:
                switchs[num] = '1' if switchs[num] == '0' else '0'
                break
            if switchs[num-j] == switchs[num+j]:
                if switchs[num-j] == '0':
                    switchs[num-j] = '1'
                    switchs[num+j] = '1'
                else:
                    switchs[num-j] = '0'
                    switchs[num+j] = '0'

for i in range(0, n, 20):
    print(' '.join(switchs[i:i+20]))