mies=["Sty","Lut","Mar","Kwi","Maj","Cze","Lip","Sie","Wrz","Paź","Lis","Gru"]
dni=[31,28,31,30,31,30,31,31,30,31,30,31]

dz_m=1
dz_t=1

for i in range(2001,2019):
    dni[1]=28
    if i%4==0:
        dni[1]=29
    for j in range(12):
        dz_m=1
        while dz_m<=dni[j]:
            dz_m+=1
            dz_t+=1
            if dz_t==8:
                dz_t=1
            if dz_m==13 and dz_t==5:
                print("13.", mies[j], i)
