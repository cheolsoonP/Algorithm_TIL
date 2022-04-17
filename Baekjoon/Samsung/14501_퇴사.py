"""
백준은 퇴사를 한다
오늘부터 N+1일 째 되는 날 퇴사를 하기 위해 남은 N일 동안 최대한 많은 상담
비서 최대한 많은 상담
N = 7일때, 8일째 되는날 퇴사
1, 2, 3, 4, 5, 6, 7일 동안 최대한 많은 상담

비서 - 하루에 하나씩 서로 다른 사람의 상담
각 상담 완료하는데 걸리는 기간 Ti
상당시 받을 수 있는 금액 Pi
최대 수익을 계산.. ->
DFS, BFS 문제. 1일을 수행 -> 이후 일정 ->
2일을 수행 -> 이후 일정
...
BFS, DFS 문제를 책으로 풀어 보고 오자.
-> DP 문제

"""


n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


def dfs(x, cost):
    if x >= n:
        return cost

    if x < n:
        dfs(graph[x][0] + x, cost + graph[x][1])



max_cost = 0
for i in range(n):
    max_cost = max(max_cost, dfs(i, 0))

print(max_cost)