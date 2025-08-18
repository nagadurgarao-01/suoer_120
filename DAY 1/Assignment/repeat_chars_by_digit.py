a=input()
l=[]
for i in a:
    l.append(i)
for i in range(len(l)):
    if l[i].isdigit():
        print(int(l[i])*l[i+1],end=" ")

  #output
   #1a2b
   #a bb
