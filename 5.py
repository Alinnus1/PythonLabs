L=[]
with open("activitati.txt") as f:
    k=1
    for x in f.readlines():
        if k==1:
            n=int(x)
            k+=1
        else:
            x=x.split()
            L.append((int(x[0]),int(x[1])))

L=sorted(L,key= lambda e: e[1])
t=0
u=0
with open("intarzieri.txt","w") as g:
    for x in L:
        g.write("{}-->{} {} {} \n".format(t,t+x[0],x[1],max(0,(t+x[0]-x[1]))))
        t=t+x[0]
