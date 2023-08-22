N=int(input())
A = list(input().split())
M=int(input())
B = list(input().split())
A.sort()

def binary_search(a, x):
    start = 0
    end = len(a) - 1
    while start <= end: 
        mid = (start + end) // 2
        if x == a[mid]:   
            return mid
        elif x > a[mid]:  
            start = mid + 1
        else:             
            end = mid - 1
    return -1 

for i in B:
    if binary_search(A, i) > -1 :
        print(1)
    else:
        print(0)