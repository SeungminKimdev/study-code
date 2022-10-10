N = input()
while(N != '0'):
    if N == N[::-1]:
        print('yes')
    else:
        print('no')
    N = input()