#include <iostream>
#include <random>

/**
 * @brief Генерирует и выводит 128-битную псевдослучайную последовательность
 *
 * @details Использует вихрь Мерсенна (Mersenne Twister) в качестве ГПСЧ.
 * Генерирует последовательность из 128 бит (0 и 1) с равномерным распределением.
 * @return int Возвращает 0 при успешном выполнении
 */

int main() {
    std::mt19937 generator(666);
    std::uniform_int_distribution<int> int_dist(0, 1);
    for (int i = 0; i < 128; i++) {
        std::cout << int_dist(generator);
    }
}