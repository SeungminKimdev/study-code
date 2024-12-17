import sys
input = sys.stdin.readline

def main():
	n = int(input())
	solution = list(map(int, input().split()))
	left = 0
	right = n - 1
	sumSolution = abs(solution[left] + solution[right])
	
	resLeft = solution[left]
	resRight = solution[right]
	while left < right:
		if abs(solution[left] + solution[right]) < sumSolution:
			sumSolution = abs(solution[left] + solution[right])
			resLeft = solution[left]
			resRight = solution[right]
		if solution[left] + solution[right] < 0:
			left += 1
		else:
			right -= 1
	print(f"{resLeft} {resRight}")

if __name__ == "__main__":
	main()