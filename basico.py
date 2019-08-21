# Coment�rio
""" Meu primeiro app """
# -- coding: utf-8  --
"""

LOGICA EM PYTHON


print("CALCULADORA EM PYTHON\n")
print("ENTRE COM PRIMEIRO N�MERO")
first = int(input())
print("ENTRE COM SEGUNDO NMERO")
second = int(input())

result = first + second
print(result)

msg = "oi"

print(msg + "." * 3)


x = 3
y = 2
a = x != y & x < 10
b = x == y | x > 10
c = x != y & x < 10

print("true " + str(b))
print("false " + str(b))
print("false " + str(b))


x = 1
y = 2

if x > y:
    print(" x e maior")
else:
    print("y e maior")


usando elif



x = 1
y = 2

if x == y:
    print(" iguais")
elif y>x:
    print("y maior")
elif y<x:
    print("x maior")
else:
    print("diferentes")

usando while
x = 1

while x < 10:
    print(x)
    x +=1


usando for

lista  = [2,4,6,8]
lista1  = ["Paulo","Bernardo","Laura","Valesca"]
lista2 = [0,"invalido",0,"incorreto"]

print("LISTA INTEIROS")
for i in lista:
    print (i+1)

print("\n\nLISTA STRINGS")
for i in lista1:
    print (i)

print("\n\nLISTA MISTA")
for i in lista2:
    print (i)

    usando range
    
for i in range(10,20,2):
    print(i)

    usando input
a = input("Seu nome: ")
print("Bem vindo "+a)

tamanho da string

a = "Paulo"
print(len(a))

navegando na string

a = "Paulo"
print(a[4])

usando range da string
a = "Paulo"
print(a[0:2])

 funcoes strings
 
a = "Paulo e Valesca Bernardo e Laura ~~"
print(a.lower())
print(a.upper())
print(a.strip())
print(a.split(" "))
print(a.find("Bernardo"))
print(a.replace("Bernardo","Lucas"))

recebendo numeros com input
a = int(input("digite um inteiro"))
b = float(input("digite um float"))

"""

