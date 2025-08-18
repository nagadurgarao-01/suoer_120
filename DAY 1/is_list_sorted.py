a = list(map(int, input().split()))
for i in range(len(a)-1):
    if a[i] > a[i+1]:
        print(False)
        break
else :
    print(True)
  
#output
#1 2 8 5 4
#False
