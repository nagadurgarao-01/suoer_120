n = input()
l =[]
for i in n:
    l.append(i)
for j in range(0,len(n)):
    for i in range(j):
        print(l[i], end ="")
    print()
for j in range(len(n), 0 ,-1):
    for i in range(j):
        print(l[i], end ="")
    print()

#output
#completed

#c
#co
#com
#comp
#compl
#comple
#complet
#complete
#completed
#complete
#complet
#comple
#compl
#comp
#com
#co
#c
