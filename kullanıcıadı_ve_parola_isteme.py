#kullanıcıadı, parola isteme
kullanıcıadı="emir"
parola=123
a=str(input("kullanıcı adınızı yazınız"))
if (a=="emir") :
    b=int(input("parolanızı yazın"))
    if (b==123) :
        input("giriş başarılı")
    else:
        print("giriş hatalı")
else:
    print("giriş hatalı")
