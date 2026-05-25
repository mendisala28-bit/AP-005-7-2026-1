// ejemplo_02_secuencia_datos_memoria.cpp
// Relacion entre ejecucion secuencial y memoria local de main.
#include <iostream>

int main() {
    int a = 10;   // Declara una variable entera llamada a y guarda el valor 10.
    int b = 20;   // Declara una variable entera llamada b y guarda el valor 20.
    int suma = 0; // Declara la variable suma y la inicializa en cero.

    suma = a + b; // Suma los valores de a y b, y guarda el resultado en suma.

    std::cout << "a = "    << a    << std::endl;
    std::cout << "b = "    << b    << std::endl;
    std::cout << "suma = " << suma << std::endl;

    return 0;
}
