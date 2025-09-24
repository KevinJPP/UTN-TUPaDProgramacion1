#1)
multiplos_de_4 = list(range(4, 101, 4))

print("Lista de múltiplos de 4 del 1 al 100:")
print(multiplos_de_4)

#2)
favoritos = ["PC", "Celular", "Fútbol", "Música", "Café"]
print("La lista es:", favoritos)
print("El penúltimo elemento es:", favoritos[-2])

#3)
lista_vacia = []

lista_vacia.append("Messi")
lista_vacia.append("Ronaldo")
lista_vacia.append("Neymar")

print("La lista final es:", lista_vacia)

#4)
animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"

animales[-1] = "oso"

print("La lista final es:", animales)

#5)
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
#El programa elimina el numero maximo de la lista y devuelve la lista sin este mismo.

#6)
numeros = list(range(10, 31, 5))
print("La lista completa es:", numeros)
print("Los dos primeros elementos son:", numeros[0], "y", numeros[1])

#7)
autos = ["sedan", "polo", "suran", "Hongolda"]

autos[1] = "BMW"
autos[2] = "Toyota"

print("La lista final es es:", autos)


#8)
dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print("La lista es:", dobles)

#9)
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

#10)
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)