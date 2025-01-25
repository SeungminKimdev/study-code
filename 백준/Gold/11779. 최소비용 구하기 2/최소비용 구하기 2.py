import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, bus, cost, parent_city):
    hq = []
    heapq.heappush(hq, (0, start)) # 비용, 도시
    while hq:
        price, city = heapq.heappop(hq)
        if cost[city] < price:
            continue
        for next_city in bus[city]:
            next_price = price + next_city[1]
            if next_price < cost[next_city[0]]:
                cost[next_city[0]] = next_price
                parent_city[next_city[0]] = city
                heapq.heappush(hq, (next_price, next_city[0]))

def find_path(end_city, parent_city):
    path = [end_city + 1]
    while parent_city[end_city] != -1:
        path.append(parent_city[end_city] + 1)
        end_city = parent_city[end_city]
    path.reverse()
    return path

def main():
    n = int(input()) # 도시의 개수
    m = int(input()) # 경로의 개수
    bus = [[] for _ in range(n)]
    cost = [INF] * n # 시작 도시로부터 해당 도시까지 최소 비용
    parent_city = [-1] * n # 해당 도시로 가는 경로 중 바로 이전 경로 저장
    
    for _ in range(m):
        start, end, price = map(int, input().split())
        bus[start-1].append((end-1, price))
    
    start_city, end_city = map(int, input().split())
    start_city -= 1
    end_city -= 1
    cost[start_city] = 0
    
    dijkstra(start_city, bus, cost, parent_city)
    answer_path = find_path(end_city, parent_city)
    print(cost[end_city])
    print(len(answer_path))
    print(*answer_path, sep=' ')

if __name__ == "__main__":
    main()