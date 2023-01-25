# G4 이중 우선순위 큐
import sys
input = sys.stdin.readline
import heapq
T = int(input())
for _ in range(T):
    k = int(input())
    min_heap, max_heap = [], []
    visited = [0]*k
    for i in range(k):
        oper, n = input().split()
        n = int(n)
        if oper == 'I':
            heapq.heappush(min_heap, (n, i))
            heapq.heappush(max_heap, (-n, i))
            visited[i] = 1 # 1이면 삭제되지 않음
        elif n==1:
            while max_heap and not visited[max_heap[0][1]]: # min_heap에서 삭제된 노드의 경우 계속 삭제 반복
                heapq.heappop(max_heap)
            if max_heap: # min_heap에서 삭제되지 않은 노드일 경우
                visited[max_heap[0][1]] = 0 # visited를 0으로 변경함으로써 삭제된 상태임을 알림
                heapq.heappop(max_heap)
        else:
            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                visited[min_heap[0][1]] = 0
                heapq.heappop(min_heap)
    # 결과 연산 전에 이미 삭제된 노드들을 다시 정리해줌
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')