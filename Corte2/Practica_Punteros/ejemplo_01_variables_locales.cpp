// ejemplo_01_variables_locales.cpp
// Variables locales declaradas dentro de main.
#include <iostream>

int main() {
    int a = 10;   // Variable local de main.
    int b = 20;   // Variable local de main.
    int suma = 0; // Variable local de main.

    suma = a + b; // Usa las variables locales para calcular un resultado.
    std::cout << "suma = " << suma << std::endl;

    return 0; // Al terminar main, sus variables locales normales dejan de ser validas.
}
