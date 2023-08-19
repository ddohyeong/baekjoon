import sys
import heapq
N = int(sys.stdin.readline())

leftheap =[]
rightheap = []

for i in range(N):
    num = int(sys.stdin.readline())
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, -num)
    else:
        heapq.heappush(rightheap,num)

    if (len(leftheap) >= 1 and len(rightheap) >= 1 and -leftheap[0] > rightheap[0]):
        leftroot = heapq.heappop(leftheap)
        heapq.heappush(rightheap, -leftroot)

        rightroot = heapq.heappop(rightheap)
        heapq.heappush(leftheap, -rightroot)

    print(-leftheap[0])