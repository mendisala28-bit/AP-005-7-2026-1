// ejemplo_07_cambio_sin_punteros.cpp
// Intento de modificar una variable desde una funcion enviando solo el valor.
// La variable original NO cambia porque la funcion recibe una copia.
// Equivalente de ejemplo_05_cambio_sin_punteros.c
#include <iostream>

void cambiar(int n) {       // n recibe una copia del valor enviado desde main.
    n = 100;                // Se modifica la copia local, no la variable original.
    std::cout << "Dentro de cambiar: n = " << n << std::endl;
}

int main() {
    int x = 5; // Variable original.

    std::cout << "Antes: x = " << x << std::endl;
    cambiar(x);  // Se envia el valor de x. La funcion recibe una copia.
    std::cout << "Despues: x = " << x << std::endl; // x no cambia.

    return 0;
}
