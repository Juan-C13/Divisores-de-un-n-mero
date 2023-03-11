n=int(input("¿Cuál es el número broder?:"))
a=0
while a<n:
    a+=1
    d=n%a
    if d==0:
        print(a)
print("Esos son todos los divisores de",n)
