// ejemplo_11_funcion_return.cpp
// Funcion que devuelve un solo resultado mediante return.
// Equivalente de ejemplo_09_funcion_return.c
#include <iostream>

int sumar(int a, int b) { // Recibe dos enteros como entrada.
    return a + b;         // Devuelve directamente un solo resultado.
}

int main() {
    int resultado = sumar(4, 7); // Llama la funcion y guarda el valor retornado.
    std::cout << "Resultado = " << resultado << std::endl;
    return 0;
}
