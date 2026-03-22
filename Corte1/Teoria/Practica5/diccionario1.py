# sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
# num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}
# print(sensors)
# print(num_cameras)
# translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch" }
# print(translations)

##Verifiying an error:
# powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3} 
# print(powers)

children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}  # Diccionario que tiene listas como valores
print(children)  # Imprime el diccionario con sus listas internas

my_empty_dictionary = {}  # Crea un diccionario vacío
print(my_empty_dictionary)  # Imprime: {}

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}  # Crea un diccionario de menú con precios
print("Before: ", menu)  # Imprime el menú antes de agregar un elemento
menu["cheesecake"] = 8  # Agrega la clave "cheesecake" con valor 8 al diccionario
print("After", menu)  # Imprime el menú con el nuevo elemento agregado

# animals_in_zoo = {"dinosaurs": 0}  # Se deja comentado: se sobreescribe 3 veces seguidas, solo quedaría el último valor
# animals_in_zoo = {"dinosaurs": 0}
# animals_in_zoo = {"horses": 2}
# print(animals_in_zoo)

##Add multiple keys
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}  # Crea un diccionario de sensores con 3 habitaciones
print("Before", sensors)  # Imprime el diccionario antes de actualizarlo
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})  # Agrega 3 nuevas entradas al diccionario de una vez
print("After", sensors)  # Imprime el diccionario con las nuevas habitaciones

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}  # Diccionario con nombres de usuario e IDs
print(user_ids)  # Imprime el diccionario inicial de usuarios
user_ids.update({"theLooper": 138475, "stringQueen": 85739})  # Agrega dos nuevos usuarios al diccionario
print(user_ids)  # Imprime el diccionario con los usuarios nuevos incluidos

## Overwrite Values ##
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}  # Recrea el diccionario menú
print("Before: ", menu)  # Imprime el menú antes de modificar el precio
menu["oatmeal"] = 5  # Sobreescribe el valor de "oatmeal" de 3 a 5
print("After", menu)  # Imprime el menú con el precio de "oatmeal" actualizado

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}  # Diccionario con ganadores del Oscar
print("Before", oscar_winners)  # Imprime los ganadores originales
print()  # Imprime una línea en blanco
oscar_winners.update({"Supporting Actress": "Viola Davis"})  # Agrega una nueva categoría con su ganadora
print("After1", oscar_winners)  # Imprime el diccionario tras agregar la nueva categoría
print()  # Imprime una línea en blanco
oscar_winners["Best Picture"] = "Moonlight"  # Corrige "Best Picture" sobreescribiendo "La La Land" por "Moonlight"
print("After2", oscar_winners)  # Imprime el diccionario con la corrección aplicada

###Dict Comprehensions
names = ['Jenny', 'Alexus', 'Sam', 'Grace']  # Lista de nombres de estudiantes
heights = [61, 70, 67, 64]  # Lista de alturas en pulgadas correspondientes a cada estudiante

zipStudents = zip(names, heights)  # Combina las dos listas en un iterador de tuplas (nombre, altura)
print("zipStudents: ", zipStudents)  # Imprime el objeto zip (muestra la referencia en memoria, no los valores)
students = {key:value for key, value in zip(names, heights)}  # Crea un diccionario nombre->altura usando comprensión
print(students)  # Imprime: {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}

drinks = ["espresso", "chai", "decaf", "drip"]  # Lista de tipos de bebidas
caffeine = [64, 40, 0, 120]  # Lista con el contenido de cafeína por bebida en miligramos
zipped_drinks = zip(drinks, caffeine)  # Combina las dos listas en un iterador de tuplas (bebida, cafeína)
print(zipped_drinks)  # Imprime el objeto zip (referencia en memoria)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}  # Crea un diccionario bebida->cafeína con comprensión
print(drinks_to_caffeine)  # Imprime el diccionario con cada bebida y su nivel de cafeína

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]  # Lista de canciones famosas
playcounts = [78, 29, 44, 21, 89, 5]  # Lista de reproducciones correspondientes a cada canción
plays = {key:value for key, value in zip(songs, playcounts)}  # Crea diccionario canción->reproducciones con comprensión
print(plays)  # Imprime el diccionario completo de canciones
plays.update({"Purple Haze": 1})  # Agrega "Purple Haze" con 1 reproducción al diccionario
plays.update({"Respect": 94})  # Actualiza las reproducciones de "Respect" de 89 a 94
print("After: ", plays)  # Imprime el diccionario con los cambios aplicados
library = {"The Best Songs": plays, "Sunday Feelings": {}}  # Crea un diccionario anidado con una playlist llena y otra vacía
print(library)  # Imprime la biblioteca completa con sus playlists
