L=[]
s=0
with open("bani.txt") as f:
    k=1
    for i in f.readlines():
        if k==1:
            L=[int(x) for x in i.split()]
            k+=1
        else:
            s=int(i)

L=sorted(L,key= lambda e: -e)
with open("plata.txt","w") as g:
    for i in L:
        c=0
        k=True
        if s>=i:
            while k==True:
                if(s-i>=0):
                    c+=1
                    s=s-i
                else:
                    k=False
            g.write(str(i)+"*"+str(c)+" ")


