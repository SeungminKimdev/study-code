def solution(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[-1] * sorted_numbers[-2]