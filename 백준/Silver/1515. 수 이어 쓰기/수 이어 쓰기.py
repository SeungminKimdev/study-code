import sys
input = sys.stdin.readline

def main():
    S = input().strip()
    length = len(S)
    
    idx = 0
    N = 0
    target_idx = 0
    
    while idx < length:
        if target_idx == 0:
            N += 1
            target_str = str(N)
        
        found_pos = target_str.find(S[idx], target_idx)
        
        if found_pos != -1:
            idx += 1
            target_idx = found_pos + 1
        else:
            target_idx = 0
    
    print(N)
    
    return

if __name__ == "__main__":
    main()