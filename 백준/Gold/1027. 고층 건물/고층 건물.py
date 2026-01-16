import sys
input = sys.stdin.readline

def main():
    N = int(input())
    hights = list(map(int, input().split()))
    look_buildings = [0] * N
    for i in range(N-1):
        inclination = hights[i+1] - hights[i]
        now_building = hights[i]
        look_buildings[i] += 1
        look_buildings[i+1] += 1
        for j in range(i+2, N):
            compare_building = hights[j]
            now_inclination = (compare_building - now_building) / (j - i)
            if now_inclination > inclination:
                inclination = now_inclination
                look_buildings[i] += 1
                look_buildings[j] += 1
    
    print(max(look_buildings))

if __name__ == "__main__":
    main()