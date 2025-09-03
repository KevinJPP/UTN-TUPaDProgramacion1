texto = input("introdude un texto: ")
vocales = "aeiouAEIOU"
contador = 0

for letra in texto:
    if letra in vocales:
        contador += 1

 

print(f"el texto contiene {contador} vocales")  


inicio = int(input("introduce el numero inicial: "))
final = int(input("introduce el numero final: "))
print(f"numeros pares del {inicio} hasta el {final}")

for numero in range (inicio, final + 1):
     if numero % 2 == 0:
      print(numero, end=" ")
