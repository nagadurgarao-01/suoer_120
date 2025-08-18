a = input()
l = list(a)
i = 0
while i < len(l):
    if l[i].isdigit():
        r1 = 0
        while l[i].isdigit() and i < len(l) :
            r1 = r1 * 10 + int(l[i])
            i += 1
        if i < len(l):
            print(l[i] * r1,end =" ")
            i += 1
    else:
        i += 1



#output

 #10a25c
#aaaaaaaaaa ccccccccccccccccccccccccc
