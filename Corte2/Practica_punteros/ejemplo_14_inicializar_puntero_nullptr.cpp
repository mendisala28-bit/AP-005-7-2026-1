// ejemplo_14_inicializar_puntero_nullptr.cpp
// Buena practica: inicializar un puntero en nullptr cuando aun no apunta a nada.
// Equivalente de ejemplo_12_inicializar_puntero_NULL.c
#include <iostream>

int main() {
    int *p = nullptr; // El puntero se inicializa en nullptr porque aun no apunta a un int.

    if (p != nullptr) { // Solo se desreferencia si apunta a una direccion valida.
        std::cout << "Valor = " << *p << std::endl;
    } else {
        std::cout << "p no apunta a una direccion valida." << std::endl;
    }

    return 0;
}
