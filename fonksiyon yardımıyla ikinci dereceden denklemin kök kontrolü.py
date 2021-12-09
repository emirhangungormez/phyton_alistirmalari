# fonksiyon yardımıyla ikinci dereceden denklemin kök kontrolü
def kök(a,b,c):
    delta=(b**2)-(4*a*c)
    if(delta==0):
        print("çift katlı kökü vardir.")
    elif(delta<0):
        print("reel kök yoktur.")
    else:
        print("iki farklı kökü vardır.")

# y=1*x**2+5*x-4
kök(1,5,4)
