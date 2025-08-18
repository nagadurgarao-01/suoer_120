#left rotation
a = input()
n = int(input())
for _ in range(n%len(a)):
     a= a[1:] + a[0]
print(a)
#output
 #acbd
 #2
#bdac
