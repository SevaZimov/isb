#include <iostream>
#include <random>

int main() {
    std::mt19937 generator(666);
    std::uniform_int_distribution<int> int_dist(0, 1);
    for (int i = 0; i < 128; i++) {
        std::cout << int_dist(generator);
    }
}