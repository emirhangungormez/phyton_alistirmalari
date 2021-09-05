#kullnıcı adı, parola isteme 2
isim="emir"
parola=123
while True:
    a=str(input("ismi giriniz:"))
    if(a==isim):
        b=int(input("parolayı giriniz:"))
        if(b==parola):
            break
        else:
            print("parola hatalı, tekrar deneyiniz")
    else:
        print("isim hatalı, tekrar deneyiniz")
print("başarılı giriş")