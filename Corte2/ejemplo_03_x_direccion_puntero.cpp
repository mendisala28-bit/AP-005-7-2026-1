// ejemplo_03_x_direccion_puntero.cpp
// Relacion entre variable, direccion y puntero.
// Equivalente de ejemplo_01_x_direccion_puntero.c
#include <iostream>

int main() {
    int x = 25;    // Variable entera con valor inicial 25.
    int *p = &x;   // p guarda la direccion de x.

    std::cout << "x  = " << x              << std::endl; // Valor directo de x.
    std::cout << "&x = " << static_cast<void*>(&x) << std::endl; // Direccion de x.
    std::cout << "p  = " << static_cast<void*>(p)  << std::endl; // Direccion en p.
    std::cout << "*p = " << *p             << std::endl; // Contenido en la direccion de p.

    return 0;
}
