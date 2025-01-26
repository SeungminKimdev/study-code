import sys
input = sys.stdin.readline

def main():
    n = int(input())
    channels = [input().strip() for _ in range(n)]

    kbs1_index = channels.index("KBS1")
    kbs2_index = channels.index("KBS2")

    result = []

    result += ['1'] * kbs1_index
    result += ['4'] * kbs1_index

    if kbs2_index < kbs1_index:
        kbs2_index += 1

    result += ['1'] * kbs2_index
    result += ['4'] * (kbs2_index - 1)

    print("".join(result))

if __name__ == "__main__":
    main()