import sys
from math import lcm, gcd

input = sys.stdin.readline

a,b = map(int, input().split())

print(gcd(a,b))
print(lcm(a,b))
