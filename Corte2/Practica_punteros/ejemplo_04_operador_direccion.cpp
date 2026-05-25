// ejemplo_04_operador_direccion.cpp
// Uso aislado del operador &: muestra valor y direccion de una variable.
// Equivalente de ejemplo_02_operador_direccion.c
#include <iostream>

int main() {
    int x = 10; // Variable entera con valor inicial 10.

    std::cout << "Valor de x    = " << x                        << std::endl;
    std::cout << "Direccion de x = " << static_cast<void*>(&x) << std::endl;

    return 0;
}
