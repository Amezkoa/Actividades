#ejercicio1
x=int(input("Escriba un número"))
y=int(input("escriba otro número"))
if x>=y*20:
  print("true")
else:
  print("false")

#ejercicio 2
num1=int(input("escribe un número"))
num2=int(input("escribe otro"))
num3=int("escribe un tercer número")
print((num1*num2*num3)/(num1+num2+num3))

#ejercicio 3
x1=int(input("escribe un número"))
x2=int(input("escribe otro"))
x3=int("escribe un tercer número")
if x1<x2<x3:
  print("true")

else:
  print("false")

#ejercicio 4
num11=int(input("escribe un número"))
num22=int(input("escribe otro"))
num33=int("escribe un tercer número")
if num11 and num22 and num33 < 0:
  print("true")

else:
  print("false")

#ejercicio 5
numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("True")
else:
    print("False")

#ejercicio 6
x11=int(input("escribe un número"))
x22=int(input("escribe otro"))
x33=int("escribe un tercer número")
if x11<x22!=x33:
  print("true")

else:
  print("false")

#ejercicio 7
n11=int(input("escribe un número"))
n22=int(input("escribe otro"))
n33=int("escribe un tercer número")
if n11==n22 or n11==n22+3:
  print("true")

else:
  print("false")

#ejercicio 8
n1=int(input("escribe un número"))
n2=int(input("escribe otro"))
n3=int(input("escribe otro"))
n4=int(input("escribe otro"))
n5=int(input("escribe otro"))
n6=int(input("escribe otro"))
n7=int(input("escribe otro"))
n8=int(input("escribe un octavo número"))
print((n1+n2+n3+n4+n5+n6+n7+n8)/(8))

#ejercicio 9
pal1=str(input("escribe una palabra"))
pal2=str(input("escribe otra"))
pal3=str(input("escribe otra"))
pal4=str(input("escribe una cuarta palabra"))
print(pal1+pal2+pal3+pal4)

#ejercicio 10
def tiene_dos_partes_pares(numero):
    return any(i % 2 == 0 and (numero - i) % 2 == 0 for i in range(numero))

numero = int(input("Ingrese el peso de la sandía (número entero positivo): "))

resultado = tiene_dos_partes_pares(numero)
print(resultado)