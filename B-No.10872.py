# src: https://www.acmicpc.net/problem/10872
N=int(input())
R=1
for i in range(1,N+1):
    R*=i

print(R)