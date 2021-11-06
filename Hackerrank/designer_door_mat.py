#Designer Door Mat Challenge
N, M = map(int,input().split(" "))
count = 1
half = (N - 1)//2

for i in range(half):
    p = ".|."*count
    print(p.center(M,"-"))
    count += 2
print("WELCOME".center(M,"-"))
count -= 2
for i in range(half):
    p = ".|."*count
    print(p.center(M,"-"))
    count -= 2