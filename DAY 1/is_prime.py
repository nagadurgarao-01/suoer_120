n = int(input())
count = 0
for i in range(1,n//2):
    if n % i+1 ==0:
        count +=1
        break
if count == 1:
    print(False)
else :
    print(True)

#output
#55
#True
