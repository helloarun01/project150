t_c=int(input())
for i in range(t_c):
    n,a,b=map(int,input().split())
    if n%2==0:
        print(min((n//2)*b , n*a))
    else:
        print(min((n//2)*b + a , n*a))