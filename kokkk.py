lista=[1,2,3,4,5,6,7,8,9,10]
q=1
while q!=0:
    for i in lista:
        if i<1000:
            lista.remove(i)
            break
