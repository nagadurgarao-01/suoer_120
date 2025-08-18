#sum of digits to single Digit
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
