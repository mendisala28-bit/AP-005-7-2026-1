// ejemplo_09_intercambio_sin_punteros.cpp
// Intento de intercambio desde una funcion sin punteros.
// Las variables originales NO cambian porque la funcion trabaja con copias.
// Equivalente de ejemplo_07_intercambio_sin_punteros.c
#include <iostream>

void intercambiar(int a, int b) { // a y b son copias locales.
    int temp = a; // Guarda temporalmente el valor de a.
    a = b;        // Cambia la copia a.
    b = temp;     // Cambia la copia b.
    std::cout << "Dentro de intercambiar: a = " << a << ", b = " << b << std::endl;
}

int main() {
    int x = 10; // Primera variable original.
    int y = 20; // Segunda variable original.

    std::cout << "Antes: x = " << x << ", y = " << y << std::endl;
    intercambiar(x, y); // Envia valores; la funcion recibe copias.
    std::cout << "Despues: x = " << x << ", y = " << y << std::endl; // No cambian.

    return 0;
}
