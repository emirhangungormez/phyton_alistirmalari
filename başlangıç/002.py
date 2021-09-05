#10dan küçük en büyük fibonacci sayısını bulma
fib1,fib2=1,1
fib=fib1+fib2
while(fib<10**1):
    fib = fib1 + fib2
    fib1=fib2
    fib2=fib
print(fib1)