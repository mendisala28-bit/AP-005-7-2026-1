// ejemplo_05_operador_contenido.cpp
// Uso del operador de desreferenciacion *: leer y modificar a traves del puntero.
// Equivalente de ejemplo_03_operador_contenido.c
#include <iostream>

int main() {
    int x = 25;  // Variable entera con valor inicial 25.
    int *p = &x; // p guarda la direccion de x.

    std::cout << "x  = " << x  << std::endl; // Valor directo de x.
    std::cout << "*p = " << *p << std::endl; // Valor en la direccion guardada en p.

    *p = 99; // Modifica x indirectamente mediante el puntero p.

    std::cout << "x despues = " << x << std::endl; // x cambia por la modificacion indirecta.

    return 0;
}
