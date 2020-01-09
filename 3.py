L=[]
with open("cuburi.txt") as f:
    k=1
    for i in f.readlines():
        if k==1:
            n=int(i)
            k+=1
        else:
            j=i.split()
            L.append((int(j[0]),j[1].strip("\n")))
L=sorted(L,key= lambda e: -e[0])
print (L)
with open("turn.txt","w") as g:
    g.write(str(L[0])+"\n")
    cc=L[0][1]
    for i in L[1:]:
        if i[1]!=cc:
            g.write(str(i)+"\n")
            cc=i[1]
