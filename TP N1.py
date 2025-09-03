#1)
print("hola mundo!")

#2)
nombre_usuario = input("porfavor, ingresa tu nombre: ")
print(f"Hola {nombre_usuario}!")

#3)
nombre = input("Por favor ingrese su nombre: ")
apellido = input("Por favor ingrese su apellido: ")
edad = input("porfavor ingrese su edad: ")
residencia = input ("porfavor ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}")

#4)
import math
radio = float(input("ingrese el radio del circulo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"El area del circulo es:  {area}" )
print(f"El perimetro del circulo es:  {perimetro}" )

#5)
segundos = float(input("ingrese los segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas.")

#6)
numero = int(input("introduce el numero: "))
print (f"\nTabla de multiplicar del {numero}: ")
for i in range(1, 11):
    print (f"{numero} x {i} = {numero} * {i}")

#7)
num1 = int(input("ingresa el primer numero entero distinto a 0: "))
while num1 == 0:
    num1 = int(input("el numero no puede ser 0, ingrese otro: "))
num2 = int(input("ingresa el segundo numero entero distinto a 0: "))
while num2 == 0:
    num2 = int(input("el numero no puede ser 0, ingrese otro: "))
suma = num1 + num2
resta = num1 - num2
division = num1 / num2
multiplicacion = num1 * num2
print(f"resultados con los numeros: {num1} y {num2}")
print(f"suma: {suma}")
print(f"resta: {resta}")
print(f"division: {division}")
print(f"multiplicacion: {multiplicacion}")


#8)
peso = float(input("ingrese su peso en kg: "))
altura = float(input("ingrese su altura en metros: "))
IMC = peso / (altura ** 2)
print(f"su indice de masa corporal es {IMC}")

#9)
celcius = float(input("ingrese la temperatura en celcius: "))
farenheint = 9/5 * (celcius) + 32
print(f"la temperatura a farenheint es: {farenheint} °")

#10)
nota1 = float(input("ingrese su primer valor: "))
nota2 = float(input("ingrese su segundo valor: "))
nota3 = float(input("ingrese su tercer valor: "))
valorF = nota1 + nota2 + nota3
promedio = valorF / 3
print (f"el promedio es: {promedio}")
