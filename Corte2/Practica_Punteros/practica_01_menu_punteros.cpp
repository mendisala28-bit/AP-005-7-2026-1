// practica_01_menu_punteros.cpp
// Practica integradora: menu interactivo que combina todas las ideas del capitulo.
// Equivalente de practica_01_menu_punteros_c.c
#include <iostream>

// --- Funcion: duplicar el valor apuntado por p ---
void duplicar(int *p) {
    if (p != nullptr) {
        *p = (*p) * 2; // Duplica el valor almacenado en la direccion apuntada.
    }
}

// --- Funcion: intercambiar los valores en dos direcciones ---
void intercambiar(int *a, int *b) {
    if (a == nullptr || b == nullptr) {
        return;
    }
    int temp = *a;
    *a = *b;
    *b = temp;
}

// --- Funcion: analizar tres numeros y escribir suma, mayor y menor ---
void analizarNumeros(int a, int b, int c, int *suma, int *mayor, int *menor) {
    if (suma == nullptr || mayor == nullptr || menor == nullptr) {
        return;
    }
    *suma = a + b + c;

    *mayor = a;
    if (b > *mayor) *mayor = b;
    if (c > *mayor) *mayor = c;

    *menor = a;
    if (b < *menor) *menor = b;
    if (c < *menor) *menor = c;
}

int main() {
    int x = 10; // Primera variable de trabajo.
    int y = 20; // Segunda variable de trabajo.
    int z = 5;  // Tercera variable de trabajo.
    int *px = &x; // px guarda la direccion de x.

    int suma;
    int mayor;
    int menor;
    int opcion;

    do {
        std::cout << "\n========== MENU CORTO DE PUNTEROS ==========" << std::endl;
        std::cout << "1. Mostrar x, &x, px y *px"                     << std::endl;
        std::cout << "2. Duplicar x usando el puntero px"             << std::endl;
        std::cout << "3. Intercambiar x y y usando punteros"          << std::endl;
        std::cout << "4. Analizar x, y, z usando punteros de salida"  << std::endl;
        std::cout << "0. Salir"                                        << std::endl;
        std::cout << "Seleccione una opcion: ";
        std::cin >> opcion;

        switch (opcion) {
            case 1:
                std::cout << "x  = " << x                         << std::endl;
                std::cout << "&x = " << static_cast<void*>(&x)    << std::endl;
                std::cout << "px = " << static_cast<void*>(px)    << std::endl;
                std::cout << "*px = " << *px                       << std::endl;
                break;

            case 2:
                std::cout << "Antes: x = " << x << std::endl;
                duplicar(px); // Modifica x usando su direccion.
                std::cout << "Despues: x = " << x << std::endl;
                break;

            case 3:
                std::cout << "Antes: x = " << x << ", y = " << y << std::endl;
                intercambiar(&x, &y); // Envia direcciones de x y y.
                std::cout << "Despues: x = " << x << ", y = " << y << std::endl;
                break;

            case 4:
                analizarNumeros(x, y, z, &suma, &mayor, &menor);
                std::cout << "Suma  = " << suma  << std::endl;
                std::cout << "Mayor = " << mayor << std::endl;
                std::cout << "Menor = " << menor << std::endl;
                break;

            case 0:
                std::cout << "Fin del programa." << std::endl;
                break;

            default:
                std::cout << "Opcion no valida." << std::endl;
                break;
        }

    } while (opcion != 0);

    return 0;
}
