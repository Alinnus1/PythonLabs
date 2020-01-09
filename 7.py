with open("obiecte.txt") as f:
    k=1
    lobiecte=[]
    for obiect in f.readlines():
        if k==1:
            n=int(obiect)
            k+=1
        else:
            valoare, greutate= obiect.split()
            lobiecte.append((int(valoare),int(greutate)))
lobiecte=sorted(lobiecte,key=lambda e: -e[0]//e[1])
h=int(input("h="))
with open("rucsac.txt","w") as g:
    g.write(f"{h}=")
    for obiect in lobiecte:
        if h>obiect[1]:
            g.write(f"{obiect[1]}+")
            h=h-obiect[1]
        elif(h==obiect[1]):
            g.write(f"{obiect[1]}+")
            break
        else:
            lasuta=h/obiect[1]
            g.write(f"{lasuta}*{obiect[1]}")
            break
