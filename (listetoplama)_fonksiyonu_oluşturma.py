#listetoplama fonksiyonu oluşturma
def listetoplama(liste):
    toplam=0
    for sayi in liste:
        toplam=toplam+sayi
    return(toplam)

print(listetoplama([9,7,13]))
