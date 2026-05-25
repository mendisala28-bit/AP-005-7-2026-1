// ejemplo_12_varios_resultados_punteros.cpp
// Punteros como canales de salida: una funcion calcula varios resultados a la vez.
// Equivalente de ejemplo_10_varios_resultados_punteros.c
#include <iostream>

void analizarNumeros(int a, int b, int c, int *suma, int *mayor, int *menor) {
    if (suma == nullptr || mayor == nullptr || menor == nullptr) {
        return; // Sale si alguna direccion no es valida.
    }
    *suma = a + b + c; // Escribe la suma en la direccion recibida.

    *mayor = a;            // Supone inicialmente que a es el mayor.
    if (b > *mayor) *mayor = b;
    if (c > *mayor) *mayor = c;

    *menor = a;            // Supone inicialmente que a es el menor.
    if (b < *menor) *menor = b;
    if (c < *menor) *menor = c;
}

int main() {
    int x = 8;   // Primer dato de entrada.
    int y = 3;   // Segundo dato de entrada.
    int z = 15;  // Tercer dato de entrada.

    int suma;    // Variable donde se escribira la suma.
    int mayor;   // Variable donde se escribira el mayor.
    int menor;   // Variable donde se escribira el menor.

    analizarNumeros(x, y, z, &suma, &mayor, &menor); // Envia valores y direcciones.

    std::cout << "Suma  = " << suma  << std::endl;
    std::cout << "Mayor = " << mayor << std::endl;
    std::cout << "Menor = " << menor << std::endl;

    return 0;
}
