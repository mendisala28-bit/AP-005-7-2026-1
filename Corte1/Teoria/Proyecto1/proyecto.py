# ============================================================
#   SISTEMA DE INVENTARIO SIMPLE
#   Programación Aplicada - Evaluación 1
# ============================================================

# --- TUPLA: información fija del sistema (categorías permitidas) ---
CATEGORIAS = ("Electrónica", "Ropa", "Alimentos", "Hogar", "Deportes", "Otros")

# --- LISTA: almacenará todos los productos registrados ---
productos = []


# ============================================================
#   FUNCIONES AUXILIARES
# ============================================================

def mostrar_bienvenida():
    """Muestra el mensaje de bienvenida al iniciar el programa."""
    print("=" * 55)
    print("   BIENVENIDO AL SISTEMA DE INVENTARIO")
    print("   Programación Aplicada - Evaluación 1")
    print("=" * 55)
    print(f"  Categorías disponibles: {', '.join(CATEGORIAS)}")
    print("=" * 55)


def mostrar_menu():
    """Imprime el menú principal de opciones."""
    print("\n" + "-" * 40)
    print("         MENÚ PRINCIPAL")
    print("-" * 40)
    print("  1. Agregar producto")
    print("  2. Mostrar todos los productos")
    print("  3. Buscar un producto")
    print("  4. Eliminar un producto")
    print("  5. Actualizar cantidad de un producto")
    print("  6. Salir del programa")
    print("-" * 40)


def codigo_existe(codigo):
    """Verifica si un código de producto ya está registrado."""
    for producto in productos:           # ciclo for para recorrer la lista
        if producto["codigo"] == codigo:
            return True
    return False


def mostrar_producto(producto):
    """Imprime la información de un producto de forma ordenada."""
    print(f"  Código   : {producto['codigo']}")
    print(f"  Nombre   : {producto['nombre']}")
    print(f"  Precio   : ${producto['precio']:.2f}")
    print(f"  Cantidad : {producto['cantidad']} unidades")
    print(f"  Categoría: {producto['categoria']}")
    print("  " + "-" * 30)


# ============================================================
#   FUNCIONES PRINCIPALES (CRUD)
# ============================================================

def agregar_producto():
    """Solicita datos al usuario y agrega un nuevo producto a la lista."""
    print("\n>>> AGREGAR PRODUCTO <<<")

    # --- Validación: código único y no vacío ---
    while True:
        codigo = input("  Ingrese el código del producto: ").strip()
        if codigo == "":
            print("  ⚠ El código no puede estar vacío.")
        elif codigo_existe(codigo):
            print("  ⚠ Ese código ya existe. Use uno diferente.")
        else:
            break

    # --- Nombre ---
    while True:
        nombre = input("  Ingrese el nombre del producto: ").strip()
        if nombre == "":
            print("  ⚠ El nombre no puede estar vacío.")
        else:
            break

    # --- Precio: conversión float() + validación ---
    while True:
        try:
            precio = float(input("  Ingrese el precio (ej. 15000.50): "))
            if precio < 0:
                print("  ⚠ El precio no puede ser negativo.")
            else:
                break
        except ValueError:
            print("  ⚠ Ingrese un número válido para el precio.")

    # --- Cantidad: conversión int() + validación ---
    while True:
        try:
            cantidad = int(input("  Ingrese la cantidad en inventario: "))
            if cantidad < 0:
                print("  ⚠ La cantidad no puede ser negativa.")
            else:
                break
        except ValueError:
            print("  ⚠ Ingrese un número entero válido para la cantidad.")

    # --- Categoría: validada contra la tupla CATEGORIAS ---
    print("\n  Categorías disponibles:")
    for i, cat in enumerate(CATEGORIAS, start=1):   # for + tupla
        print(f"    {i}. {cat}")

    while True:
        try:
            opcion_cat = int(input("  Seleccione el número de categoría: "))
            if 1 <= opcion_cat <= len(CATEGORIAS):
                categoria = CATEGORIAS[opcion_cat - 1]
                break
            else:
                print(f"  ⚠ Ingrese un número entre 1 y {len(CATEGORIAS)}.")
        except ValueError:
            print("  ⚠ Ingrese un número válido.")

    # --- DICCIONARIO: representa el producto ---
    nuevo_producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria
    }

    productos.append(nuevo_producto)   # se agrega a la lista
    print(f"\n  ✔ Producto '{nombre}' agregado correctamente.")


def mostrar_todos():
    """Muestra todos los productos registrados en el inventario."""
    print("\n>>> LISTA DE PRODUCTOS <<<")

    if len(productos) == 0:             # condicional if
        print("  No hay productos registrados aún.")
    else:
        print(f"  Total de productos: {len(productos)}\n")
        for producto in productos:      # ciclo for sobre la lista
            mostrar_producto(producto)


def buscar_producto():
    """Busca un producto por código o por nombre (parcial)."""
    print("\n>>> BUSCAR PRODUCTO <<<")
    termino = input("  Ingrese código o nombre a buscar: ").strip().lower()

    if termino == "":
        print("  ⚠ Ingrese un término de búsqueda.")
        return

    encontrados = []
    for producto in productos:          # ciclo for para recorrer la lista
        if (termino in producto["codigo"].lower() or
                termino in producto["nombre"].lower()):
            encontrados.append(producto)

    if len(encontrados) == 0:           # if / else
        print("  No se encontraron productos con ese criterio.")
    else:
        print(f"  Se encontraron {len(encontrados)} resultado(s):\n")
        for p in encontrados:
            mostrar_producto(p)


def eliminar_producto():
    """Elimina un producto del inventario a partir de su código."""
    print("\n>>> ELIMINAR PRODUCTO <<<")

    if len(productos) == 0:
        print("  No hay productos para eliminar.")
        return

    codigo = input("  Ingrese el código del producto a eliminar: ").strip()

    indice_a_eliminar = None
    for i, producto in enumerate(productos):   # for con índice
        if producto["codigo"] == codigo:
            indice_a_eliminar = i
            break

    if indice_a_eliminar is None:              # if / elif / else
        print("  ⚠ No se encontró un producto con ese código.")
    else:
        nombre_eliminado = productos[indice_a_eliminar]["nombre"]
        confirmacion = input(
            f"  ¿Desea eliminar '{nombre_eliminado}'? (s/n): "
        ).strip().lower()

        if confirmacion == "s":
            productos.pop(indice_a_eliminar)
            print(f"  ✔ Producto '{nombre_eliminado}' eliminado correctamente.")
        elif confirmacion == "n":
            print("  Operación cancelada.")
        else:
            print("  Opción no válida. Operación cancelada.")


def actualizar_cantidad():
    """Suma o resta unidades a un producto existente."""
    print("\n>>> ACTUALIZAR CANTIDAD <<<")

    if len(productos) == 0:
        print("  No hay productos registrados.")
        return

    codigo = input("  Ingrese el código del producto: ").strip()

    # Buscar el producto en la lista
    producto_encontrado = None
    for producto in productos:
        if producto["codigo"] == codigo:
            producto_encontrado = producto
            break

    if producto_encontrado is None:
        print("  ⚠ No se encontró un producto con ese código.")
        return

    print(f"\n  Producto    : {producto_encontrado['nombre']}")
    print(f"  Stock actual: {producto_encontrado['cantidad']} unidades")
    print("\n  ¿Qué desea hacer?")
    print("    1. Retirar unidades  (venta / salida)")
    print("    2. Agregar unidades  (compra / entrada)")

    tipo = input("  Seleccione (1/2): ").strip()

    if tipo not in ("1", "2"):
        print("  ⚠ Opción no válida.")
        return

    while True:
        try:
            cantidad = int(input("  Ingrese la cantidad de unidades: "))
            if cantidad <= 0:
                print("  ⚠ Ingrese un número mayor a cero.")
            else:
                break
        except ValueError:
            print("  ⚠ Ingrese un número entero válido.")

    if tipo == "1":                                      # retirar
        if cantidad > producto_encontrado["cantidad"]:
            print(f"  ⚠ No hay suficiente stock. Disponible: {producto_encontrado['cantidad']} unidades.")
        else:
            producto_encontrado["cantidad"] -= cantidad
            print(f"  ✔ Se retiraron {cantidad} unidades. Stock actual: {producto_encontrado['cantidad']}.")
    elif tipo == "2":                                    # agregar
        producto_encontrado["cantidad"] += cantidad
        print(f"  ✔ Se agregaron {cantidad} unidades. Stock actual: {producto_encontrado['cantidad']}.")


# ============================================================
#   PROGRAMA PRINCIPAL
# ============================================================

def main():
    mostrar_bienvenida()

    # --- CICLO WHILE: mantiene el menú en ejecución ---
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("  Seleccione una opción (1-6): ").strip()

        # --- CONDICIONALES if / elif / else ---
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_todos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            actualizar_cantidad()
        elif opcion == "6":
            print("\n  ¡Hasta luego! El sistema ha sido cerrado correctamente.")
            print("=" * 55)
            continuar = False
        else:
            print("  ⚠ Opción no válida. Ingrese un número entre 1 y 6.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
