#Ejercicio 1
cor= int(input("Inserte la corriende del circuito"))
res= int(input("Inserte la resistencia del circuito"))
voltaje= cor * res
print("El voltaje es de: ", voltaje)

#Ejercicio 2
p1= int(input("Inserta el precio de los boletos del año pasado"))
p2= int(8000)
dif1= p1-p2
por= p1// p2
dif2= p2-p1
if p1>p2:
  print("la diferencia de precio entre los boletos es de: ", dif1)
  print("El valor del boleto actual es de", por, "respecto al del año pasado")
elif p2> p1:
  print("la diferencia de precio de los boletos es de: ", dif2)
  print("El valor del boleto actual es de", por, "respecto al del año pasado")


#Ejercicio 3
num= float(input("Inserte un número para saber si es par o impar"))
if num%2 == 0:
  print("El número insertado es par")
else:
  print("El número insertado es impar")

#Ejercicio 4
libros= ["Biblia", "Corán", "Principito", "El diario de Greg", "Programación en Python", "Algoritmos avanzados", "Algebra de Baldor"]
libros.append(str("El señor de los anillos"))
libros.append(str("Harry Potter"))
libros.append(str("El contrato social"))
libros.append(str("Star Wars"))
libros.pop
libros.pop
libros.index("El diario de Greg")
libros.index("Biblia")

#Ejercicio 5


#Teoría
#6. Append e insert.
#7. len
#8. Es uno de los diferentes tipos de dato que existe. El string se utiliza para palabras o secuencias de letras.
#9. String: Se utiliza para palabras o secuencias de letras
#integer: Se utiliza para números sin decimales.
#Float: Se utiliza para números con decimales.
# Booleano: Se utiliza para valores de true y false.
#10. Una variables es un valor que puede ser asignado por el usuario o que ya fue previamente determinado y que se utiliza para generar un cambio o determinar la forma en la que el algoritmo procede.
#11. La diferencia es el cómo trabajan: And utiliza "y", lo que nos dice que tienen que cumplirse dos o más condiciones; or utiliza "o" lo que nos dice que una y otra condición se tiene que cumplir y Not utiliza "no" lo que nod dice que no tiene que cumplirse la condición.

#Ejercicio 12
lado=int(input("Escribe el valor de un lado del triángulo: "))
altura= ((lado*1.73205080757)/(2))
area= ((lado*altura)/(2))
print("El área del triángulo es:", area)
#Ejercicio 13
texto= str(input("Escribe un texto:"))
if len(texto)<500 or len(texto)== 500:
  print("Bien hecho, tienes menos de 500 palabras")
else: 
  print("error")