#right rotation
a = input()
n = int(input())
for _ in range(n%len(a)):
     a= a[-1] + a[:-1]
print(a)

#output
 #abcd
# 2
#cdab

#right rotation
a = input()
n = int(input())
n = n % len(a)
a = a[-n:] + a[:-n]
print(a)
