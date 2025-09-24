#1)
edad = float(input("introduzca su edad: "))
if edad >= 18:
    print("usted es mayor de edad")

#2)
nota = float (input("introduzca su nota: "))
if nota >= 6:
    print("usted esta aprobado")
elif nota < 6:
 print("usted esta desaprobado")

#3)
numero = int(input("introduzca un numero: "))
if numero % 2 == 0:
      print("usted a ingresado un numero par")
else:
      print("por favor ingrese un numero par")

#4)
edad = int(input("introduzca su edad: "))
if edad < 12:
 print ("usted es un niño/a")
elif 12 <= edad < 18:
 print ("usted es un adolescente")
elif 18 <= edad < 30:
 print ("usted es un adulto/a joven")         
elif 30 <= 100:
   print ("usted es un adulto/a")

#5) 

contraseña = input("ingrese la contraseña: ")
longitud = len(contraseña)
if 8 <= longitud <= 14:
   print ("Ha ingresado una contraseña correcta")
   
else:
   print ("por favor, ingrese una contraseña de entre 8 a 14 elementos")   

#6)
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
try:
    moda = mode(numeros_aleatorios)
except:
    moda = None
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"La lista de números aleatorios es:\n{numeros_aleatorios}\n")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana}")

if moda is not None:
    print(f"Moda: {moda}")
    
    if media > mediana and mediana > moda:
        sesgo = "positivo o a la derecha"
    elif media < mediana and mediana < moda:
        sesgo = "negativo o a la izquierda"
    elif media == mediana and mediana == moda:
        sesgo = "sin sesgo"
    else:
        sesgo = "no se puede determinar con el criterio dado"
else:
    sesgo = "no se puede determinar con el criterio dado (múltiples modas)"

print(f"\nEl sesgo de la distribución es: {sesgo}.")




#7)
frase = (input("ingrese una frase: "))
vocales = "aeiouAEIOU"
if frase[-1] in vocales:
    frase_final = frase + "!"
else:
     frase_final = frase
print(frase_final)

#8)
nombre = input("ingrese su nombre: ")
opcion = input("elige una opcion (1, 2 o 3) : /n1 Nombre en mayusculas / n2 Nombre en minusculas / n3 Primera letra en mayuscula: ")

if opcion == '1':
    nombre_final = nombre.upper()
elif opcion == '2':
    nombre_final = nombre.lower()
elif opcion == '3':
    nombre_final = nombre.title()            
print (nombre_final)

#9)

magnitud = float(input("ingrese la magnitud del terremoto: "))
if magnitud < 3:
   print ("muy leve")
elif 3 <= magnitud < 4:
   print ("leve")
elif 4 <= magnitud < 5:
   print ("moderado")
elif 5 <= magnitud < 6:
   print ("fuerte")
elif 6 <= magnitud < 7:
   print ("muy fuerte")
elif magnitud >= 7:
   print ("extremo")

#10)
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

estacion = ""

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion = "Invierno" if hemisferio == "N" else "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
     estacion = "Primavera" if hemisferio == "N" else "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
     estacion = "Verano" if hemisferio == "N" else "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
     estacion = "Otoño" if hemisferio == "N" else "Primavera"
print ("tu ubicacion esta en ", estacion)          