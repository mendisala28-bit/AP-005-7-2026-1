// ejemplo_10_intercambio_con_punteros.cpp
// Intercambio correcto usando punteros: la funcion recibe direcciones.
// Equivalente de ejemplo_08_intercambio_con_punteros.c
#include <iostream>

void intercambiar(int *a, int *b) { // a y b reciben direcciones de variables enteras.
    if (a == nullptr || b == nullptr) { // Verifica si alguna direccion no es valida.
        return;
    }
    int temp = *a; // Guarda el contenido apuntado por a.
    *a = *b;       // Escribe en la direccion a el contenido de b.
    *b = temp;     // Escribe en la direccion b el valor temporal.
}

int main() {
    int x = 10; // Primera variable original.
    int y = 20; // Segunda variable original.

    std::cout << "Antes: x = " << x << ", y = " << y << std::endl;
    intercambiar(&x, &y); // Envia las direcciones de x y y.
    std::cout << "Despues: x = " << x << ", y = " << y << std::endl; // Ahora cambian.

    return 0;
}
