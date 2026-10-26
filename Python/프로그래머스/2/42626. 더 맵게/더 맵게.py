import heapq

def solution(scoville, K):
    heap = scoville[:]
    heapq.heapify(heap)
    count = 0

    while heap[0] < K:
        if len(heap) < 2:
            return -1
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        mixed = first + second * 2
        heapq.heappush(heap, mixed)
        count += 1

    return count