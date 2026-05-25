// ejemplo_08_cambio_con_direccion.cpp
// Modificacion de una variable desde una funcion enviando su direccion.
// La variable original SI cambia porque la funcion escribe en su direccion.
// Equivalente de ejemplo_06_cambio_con_direccion.c
#include <iostream>

void cambiar(int *p) {      // p recibe una copia de una direccion.
    if (p == nullptr) {     // Verifica si la direccion recibida no es valida.
        return;             // Sale de la funcion para evitar usar un puntero invalido.
    }
    *p = 100;               // Escribe 100 en la variable ubicada en la direccion recibida.
}

int main() {
    int x = 5; // Variable original.

    std::cout << "Antes: x = " << x << std::endl;
    cambiar(&x);  // Envia la direccion de x.
    std::cout << "Despues: x = " << x << std::endl; // x cambia.

    return 0;
}
