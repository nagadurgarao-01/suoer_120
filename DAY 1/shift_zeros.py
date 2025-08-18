n = list(map(int , input().split()))
for i in range(len(n)):
    if n[i]==0:
        a =n[i]
        n.remove(a)
        n.append(a)
print(n)   

# output
 #1 0 1 0 1 02 3 0
 #[1, 1, 1, 2, 3, 0, 0, 0]
