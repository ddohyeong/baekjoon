from bisect import bisect_left, bisect_right
import sys
# input = sys.stdin.readline

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index



N = int(input())
n_data = list(map(int, input().split()))
M = int(input())
m_data = list(map(int, input().split()))
n_data.sort()

for i in range(len(m_data)):
    print(count_by_range(n_data, m_data[i],m_data[i]), end=" ")

