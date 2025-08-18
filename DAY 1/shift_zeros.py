n = list(map(int , input().split()))
for i in range(len(n)):
    if n[i]==0:
        a =n[i]
        n.remove(a)
        n.append(a)
print(n)   
