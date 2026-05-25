// ejemplo_13_puntero_y_arreglo_basico.cpp
// Primera relacion entre un arreglo, su primer elemento y un puntero.
// Equivalente de ejemplo_11_puntero_y_arreglo_basico.c
#include <iostream>

int main() {
    int datos[3] = {10, 20, 30}; // Arreglo de tres enteros.
    int *p = datos;              // p apunta al primer elemento del arreglo.

    std::cout << "datos[0]   = " << datos[0]   << std::endl; // Acceso mediante indice.
    std::cout << "*p         = " << *p         << std::endl; // Acceso mediante puntero.
    std::cout << "*(p + 1)   = " << *(p + 1)   << std::endl; // Segundo elemento.
    std::cout << "*(p + 2)   = " << *(p + 2)   << std::endl; // Tercer elemento.

    return 0;
}
