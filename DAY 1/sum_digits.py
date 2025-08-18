n = int(input())
s = 0
while n!=0:
    a = n%10
    s += a
    n = n//10
print(s)

#output

# 23232
#12
#logic 2

n = int(input())
sum = 0
while n > 9:
    n = str(n)
    for i in n:
        sum += int(i)
    n = sum
print(sum)

#output

# 23232
#12
