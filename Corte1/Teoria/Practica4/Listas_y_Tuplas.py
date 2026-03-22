#################LISTAS####################
###########################################
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']  # Crea una lista de strings con 6 colores
#input()  # Línea comentada: pausaría la ejecución esperando input del usuario
print(my_lista)  # Imprime toda la lista
print(type(my_lista))  # Imprime el tipo de dato: <class 'list'>
print(my_lista[2])  # Imprime el elemento en el índice 2: 'Amarillo'
print("my_lista size: ", len(my_lista))  # Imprime la cantidad de elementos de la lista
print(my_lista[0:2])  # Imprime un slice de los índices 0 al 1 (no incluye el 2)
print(my_lista[:2])  # Imprime un slice desde el inicio hasta el índice 1
my_lista.append('Blanco')      # Agrega 'Blanco' al final de la lista
print(my_lista)  # Imprime la lista con el nuevo elemento agregado
my_lista.insert(3, 'Negro')  # Inserta 'Negro' en el índice 3
print(my_lista)  # Imprime la lista con 'Negro' insertado
my_lista.extend(['Marron', 'Gris'])   # Agrega los elementos de otra lista al final
print(my_lista)  # Imprime la lista después de extenderla
print(my_lista.index('Azul'))  # Imprime el índice donde se encuentra 'Azul'
#my_lista.remove('Magenta')  
my_lista.remove('Marron')  # Elimina la primera ocurrencia de 'Marron'
print(my_lista)  # Imprime la lista sin 'Marron'
my_lista.insert(8, 'Marron')  # Reinserta 'Marron' en el índice 8
print(my_lista)  # Imprime la lista con 'Marron' en su nueva posición
print(my_lista.pop())  # Elimina y imprime el último elemento de la lista
size = len(my_lista)  # Guarda la cantidad de elementos actuales en la variable size
print("size = ", size)  # Imprime el tamaño actual de la lista
#print(my_lista.pop(size)) 
my_lista_3 = my_lista*3  # Crea una nueva lista repitiendo my_lista 3 veces
print("my_lista_3: ", my_lista_3)  # Imprime la lista triplicada
print("Sort:")  # Imprime el texto "Sort:"
print()  
my_listaSort = my_lista.sort()  # Ordena my_lista en su lugar (devuelve None)
print(my_listaSort)  # Imprime None, porque .sort() no retorna la lista
my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]  # Crea una lista de números del 10 al 1
print("Ordering my_NumList: ")  # Imprime texto indicativo
my_NumList.sort()  # Ordena my_NumList de menor a mayor en su lugar
print(my_NumList)  # Imprime la lista ordenada ascendentemente
#OrderedLList = my_NumList.sort()  
#print(my_listaSort)  
my_NumList.sort(reverse = True)  # Ordena la lista de mayor a menor
print("De menor a mayor: ", my_NumList)  # Imprime la lista en orden descendente

#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:
# Convertir una lista a tupla:
print("###########################")  # Imprime separador visual
print("###########################")  
print("###########################")  
print("############TUPLAS#########") 
my_tupla = tuple(my_lista)  # Convierte my_lista en una tupla inmutable
print()  # Imprime línea en blanco
print()  # Imprime línea en blanco
print("my_tuple: ", my_tupla)  # Imprime la tupla completa
print(my_tupla[0])  # Imprime el primer elemento de la tupla
print(my_tupla[2])  # Imprime el elemento en el índice 2
print('Rojo' in my_tupla)  # Imprime True si 'Rojo' está en la tupla, False si no
print(my_tupla.count('Rojo'))  # Imprime cuántas veces aparece 'Rojo' en la tupla
my_tupla_unitaria = ('Blanco')  # Crea un string, NO una tupla (falta la coma)
print(my_tupla_unitaria)  # Imprime 'Blanco' como string
my_tupla = 'Gaspar', 5, 8, 1999  # Crea una tupla sin paréntesis (empaquetado)
print(my_tupla)  # Imprime la tupla empaquetada
nombre, dia, mes, año = my_tupla  # Desempaqueta la tupla en 4 variables individuales
print(nombre)  # Imprime 'Gaspar'
print(dia)  # Imprime 5
print(mes)  # Imprime 8
print(año)  # Imprime 1999
print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)  # Imprime todos los valores formateados
my_lista2 = list(my_tupla)  # Convierte la tupla de nuevo en una lista
print(my_lista2)  # Imprime la lista resultante de la conversión
