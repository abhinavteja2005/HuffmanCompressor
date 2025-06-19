#include <iostream>
#include "encoder.hpp"
#include "decoder.hpp"

int main(int argc, char* argv[]) {
    if (argc != 4) {
        std::cerr << "Usage:\n";
        std::cerr << "  " << argv[0] << " -c input.txt output.huff    # compress\n";
        std::cerr << "  " << argv[0] << " -d input.huff output.txt    # decompress\n";
        return 1;
    }

    std::string option = argv[1];
    std::string inputFile = argv[2];
    std::string outputFile = argv[3];

    if (option == "-c") {
        compressFile(inputFile, outputFile);
        std::cout << "Compressed successfully: " << outputFile << "\n";
    } else if (option == "-d") {
        decompressFile(inputFile, outputFile);
        std::cout << "Decompressed successfully: " << outputFile << "\n";
    } else {
        std::cerr << "Unknown option: " << option << "\n";
        return 1;
    }

    return 0;
}
