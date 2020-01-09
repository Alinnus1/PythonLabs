with open("proiecte.txt") as f:
    L=[]
    for proiect in f.readlines():
        nume,termenl,profit= proiect.split()
        L.append((nume,int(termenl),int(profit)))

L=sorted(L,key= lambda e: -e[2])
T=0
T1=max(x[1] for x in L)
print(T1)
with open("profit.txt","w") as g:
    for proiect in L:
        if proiect[1]>=T:
            g.write(proiect[0])
            T+=1

