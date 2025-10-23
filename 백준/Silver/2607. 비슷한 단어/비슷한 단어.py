import sys
from collections import Counter
input = sys.stdin.readline

def main():
    n = int(input().strip())
    main_word = input().strip()
    main_counter = Counter(main_word) 
    answer = 0
    
    for _ in range(n - 1):
        word = input().strip()
        word_counter = Counter(word)
        len_diff = abs(len(main_word) - len(word))
        if len_diff > 1:
            continue
        
        diff_count = sum((main_counter - word_counter).values()) + sum((word_counter - main_counter).values())
        if len_diff == 0 and diff_count == 0:
            answer += 1
        elif len_diff == 1 and diff_count == 1:
            answer += 1
        elif len_diff == 0 and diff_count == 2:
            answer += 1
    
    print(answer)
    return

if __name__ == "__main__":
    main()