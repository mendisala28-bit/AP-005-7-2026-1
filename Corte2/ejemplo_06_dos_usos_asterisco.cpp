// ejemplo_06_dos_usos_asterisco.cpp
// El simbolo * en dos contextos: declaracion y desreferenciacion.
// Equivalente de ejemplo_04_dos_usos_asterisco.c
#include <iostream>

int main() {
    int x = 5;   // Variable entera con valor inicial 5.
    int *p = &x; // Declaracion de puntero: aqui * forma parte de la declaracion.

    *p = 40;     // Desreferenciacion: aqui * accede al contenido apuntado por p.

    std::cout << "x = " << x << std::endl; // Muestra el valor final de x.

    return 0;
}
