x=int(input())
num=[[0]*2 for k in range(x)]
for i in range(x):
    num[i]=list(map(int,input().split()))
num.sort(key=lambda x:(x[1], x[0]))
for i in range(x):
    print("%d %d"%(num[i][0],num[i][1]))