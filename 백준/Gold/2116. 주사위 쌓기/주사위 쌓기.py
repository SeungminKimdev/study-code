from collections import deque
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    dices = [0] * 6 #
    a, b, c, d, e, f = map(int, input().split())
    dices[a-1] = max([b,c,d,e])
    dices[b-1] = max([a,c,e,f])
    dices[c-1] = max([a,b,d,f])
    dices[d-1] = dices[b-1]
    dices[e-1] = dices[c-1]
    dices[f-1] = dices[a-1]
    
    for _ in range(n-1):
        a, b, c, d, e, f = map(int, input().split())
        a_f = max([b,c,d,e])
        b_d = max([a,c,e,f])
        c_e = max([a,b,d,f])
        new_dices = [0] * 6
        new_dices[a-1] = dices[f-1] + a_f
        new_dices[b-1] = dices[d-1] + b_d
        new_dices[c-1] = dices[e-1] + c_e
        new_dices[d-1] = dices[b-1] + b_d
        new_dices[e-1] = dices[c-1] + c_e
        new_dices[f-1] = dices[a-1] + a_f
        dices = new_dices

    print(max(dices))

if __name__ == "__main__":
    main()
