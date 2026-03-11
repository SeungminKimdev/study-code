def solution(strArr):
    words = {i:0 for i in range(1,31)}
    for strA in strArr:
        words[len(strA)] += 1
    return max(words.values())