#Ejercicio 1
numero = int(input("Ingrese un número: "))
suma = 0

for i in range(numero + 1):
    suma += i

print("La suma de 0 a", numero, "es:", suma)


#Ejercicio 2
total = 0
contador = 0

while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    
    if numero == 0:
        break
    
    total += numero
    contador += 1

if contador == 0:
    print("No se introdujeron números.")
else:
    promedio = total / contador
    print("El promedio de los números introducidos es:", promedio)


#Ejercicio 3
n = int(input("Ingrese la cantidad de artículos: "))
articulos = []

for i in range(n):
    articulo = input(f"Ingrese el nombre del artículo {i + 1}: ")
    articulos.append(articulo)

articulos.sort() 

print("\nLista de compras en orden alfabético:")
for articulo in articulos:
    print(articulo)


#Ejercicio 4
n = int(input("Ingrese la cantidad de números en la lista: "))
numeros = []

for i in range(n):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

numeros_pares = [numero for numero in numeros if numero % 2 == 0]

print("\nLista de números pares:")
for numero in numeros_pares:
    print(numero)


#Ejercicio 5
entrada = input("Ingrese una frase: ")
vocales = "aeiouAEIOU" 

vocales_encontradas = [letra for letra in entrada if letra in vocales]

resultado = ''.join(vocales_encontradas)

print("Vocales encontradas:", resultado)


#Ejercicio 6
def es_divisible_por_243(numero):
    if numero % 243 == 0:
        return True
    else:
        return False

numero = int(input("Ingrese un número: "))

if es_divisible_por_243(numero):
    print(f"{numero} es divisible por 243.")
else:
    print(f"{numero} no es divisible por 243.")


#Ejercicio 7
def multiplicarString(cadena, n):
    if n <= 0:
        return ""
    else:
        resultado = cadena * n
        return resultado

cadena = input("Ingrese un string: ")
n = int(input("Ingrese un número entero positivo: "))

resultado = multiplicarString(cadena, n)
print("Resultado:", resultado)


#Ejercicio 8
def calcular_resultado(a, b, c):
    if a > 100 or b > 100 or c > 100:
        return a + b + c
    else:
        return a * b * c

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

resultado = calcular_resultado(numero1, numero2, numero3)
print("Resultado:", resultado)


#Ejercicio 9
def es_puras_vocales(cadena):
    return all(letra in "aeiouAEIOU" for letra in cadena)

def es_puras_consonantes(cadena):
    return all(letra.isalpha() and letra not in "aeiouAEIOU" for letra in cadena)

def stringsExclusivos(str1, str2):
    if (es_puras_vocales(str1) and es_puras_consonantes(str2)) or (es_puras_consonantes(str1) and es_puras_vocales(str2)):
        return True
    else:
        return False

cadena1 = input("Ingrese el primer string: ")
cadena2 = input("Ingrese el segundo string: ")

resultado = stringsExclusivos(cadena1, cadena2)
print("Resultado:", resultado)


#Ejercicio 10
def esPalindromo(cadena):
    cadena = cadena.lower()  
    cadena = ''.join(c for c in cadena if c.isalnum())  
    return cadena == cadena[::-1]

cadena = input("Ingrese una cadena: ")

resultado = esPalindromo(cadena)
if resultado:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")

