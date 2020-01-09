import re
L=[]
with open("spectacole.txt") as f:
    for x in f.readlines():
        x=x.split("-")
        x[1]=x[1].split(" ",1)
        L.append((x[0],x[1][0],x[1][1].strip("\n")))
with open("programare.txt","w") as g:
    L= sorted(L,key= lambda e :e[1] )
    print(L)
    g.write(str(L[0])+"\n")
    deadline=L[0][1]
    for i in L[1:]:
        if i[0]>deadline:
            g.write(str(i)+"\n")
            deadline=i[0]