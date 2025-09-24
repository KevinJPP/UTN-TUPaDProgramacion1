#1)
for i in range(1, 101):
 print (i)

#2)
numero = input("introduce un numero entero: ")
cantidad_digitos = len(numero)
print(f"el numero tiene {cantidad_digitos}")

#3)
valor1 = int(input("Introduce el primer número: "))
valor2 = int(input("Introduce el segundo número: "))
if valor1 > valor2:
    valor1, valor2 = valor2, valor1
suma = 0
for i in range(valor1 + 1, valor2):
    suma += i
print("La suma de los números entre", valor1, "y", valor2, "es:", suma)

#4)
suma = 0
numero = None
while numero != 0:
    numero = int(input("Ingresa un número entero (0 para finalizar): "))
    suma += numero

print("La suma total es:", suma)

#5)
import random

numero_secreto = random.randint(0, 9)
intentos = 0
adivinado = False

print("Bienvenido al juego de adivinar el número")
print("Intenta adivinar un número entre 0 y 9.")

while not adivinado:
    intento = int(input("Tu intento: "))
    intentos += 1
    
    if intento == numero_secreto:
        adivinado = True
    else:
        print("No adivinaste, intenta de nuevo.")

print("Adivinaste, El número era", numero_secreto)
print("Usaste", intentos, "intentos para adivinarlo.")

#6)
for i in range(100, -1, -2):
    print(i)

#7)
numero = int(input("Ingresa un número entero positivo: "))

suma = 0
for i in range(numero + 1):
    suma += i

print("La suma de los números entre 0 y", numero, "es:", suma)

#8)
CANTIDAD = 100  

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(CANTIDAD):
    num = int(input(f"Ingrese el número {i+1}: "))

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1


print("Resultados:")
print("Números pares:", pares)
print("Números impares:", impares)
print("Números positivos:", positivos)
print("Números negativos:", negativos)

#9)
cantidad = 100

suma = 0

for i in range(cantidad):
    num = int(input(f"Ingrese el número {i+1}: "))
    suma += num

media = suma / cantidad

print("\nLa media de los", cantidad, "números ingresados es:", media)

#10)
numero = input("Ingresa un número entero: ")
invertido = numero[::-1] 
print("número invertido:", invertido)

