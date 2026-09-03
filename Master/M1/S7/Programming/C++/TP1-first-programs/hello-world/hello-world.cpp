// This header file must be included for input output functions
// e.g. here cout and endl
#include <iostream>

int main() {
    
    // This statement prints "Hello World" and ends the line
    // Notice that cout and endl are part of the std namespace, therefore we need specify
    // that with :: operator before.
    // This can be avoided by adding "using namespace std;" at the beginning
    // But this is not always recommanded
    std::cout << "Hello world !" << std::endl;

    // The program was successful, we return EXIT_SUCCESS
    // This is the same as writing "return 0;" 
    return EXIT_SUCCESS; 
}