from queue import PriorityQueue
import sys

input = sys.stdin.readline

max_que = PriorityQueue()
min_que = PriorityQueue()


n = int(input())

for i in range(n):
    num = int(input())
    if num == 0:
        if min_que.empty() and max_que.empty():
            print(0)
        elif min_que.empty():
            print(-1 * max_que.get())
        elif max_que.empty():
            print(min_que.get())
        else:
            a = max_que.get()
            b = min_que.get()

            if  a == b:
                print(-a)
                min_que.put(b)
            elif a < b:
                print(-a)
                min_que.put(b)
            elif a > b:
                print(b)
                max_que.put(a)
    elif num > 0:
        min_que.put(num)
    else:
        max_que.put(-num)
    



