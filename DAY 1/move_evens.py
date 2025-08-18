n = list(map(int , input().split()))
for i in range(len(n)):
    if n[i] %2 ==0:
        a =n[i]
        n.remove(a)
        n.append(a)
print(n) 


#output

# 2 3 11 58 333 222 121 45454
#[3, 11, 333, 121, 2, 222, 58, 45454]
