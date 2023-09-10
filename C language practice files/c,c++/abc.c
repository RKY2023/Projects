// #include <iostream>
// #include <chrono>
// #include <thread>

// int main() {
//     while (true) {
//         std::cout << "hello" << std::endl;
//         // std::this_thread::sleep_for(std::chrono::seconds(5));
//     }
//     return 0;
// }
#include <stdio.h>

int main() {
    int v;
    scanf("Enter a value: %d",&v); 
    if (v == 2) {
        printf("hello");
    }
    return 0;
}