#n faktöriyel bulma
fakt=1
while True:
    n=int(input("sayı giriniz:"))
    if(n<0):
        print("pozitif sayı giriniz")
    else:
        for i in range(1,n+1):
            fakt=fakt*i
        break
print(fakt)