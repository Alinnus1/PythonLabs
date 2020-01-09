f=open("tis.txt")
L=[]
j=1
linie=f.readline()
for i in linie.split(" "):
    L.append((j,int(i)))
    j+=1
f.close()
def afisare_timpi_servire(L):
    timpasteptare=0
    k=0
    s=0
    for i in L:
        timpasteptare+=i[1]
        k+=1
        s+=timpasteptare
        print(i[0],i[1],timpasteptare)

    print(s/k)

print(L)

L=sorted(L,key= lambda e: e[1])

afisare_timpi_servire(L)