#include "decoder.hpp"
#include <fstream>
#include <bitset>
#include <iostream>
#include <cstdint>


// Read the code table from file and rebuild the tree
HuffmanNode* readCodeTable(std::ifstream& in) {
    size_t tableSize;
    in.read(reinterpret_cast<char*>(&tableSize), sizeof(tableSize));

    std::unordered_map<std::string, char> codeToChar;

    for (size_t i = 0; i < tableSize; ++i) {
        char ch = in.get();
        uint8_t codeLen = in.get();
        std::string code = "";

        int totalBits = codeLen;
        while (totalBits > 0) {
            char byte = in.get();
            for (int j = 0; j < 8 && totalBits > 0; ++j, --totalBits) {
                code += ((byte >> (7 - j)) & 1) ? '1' : '0';
            }
        }

        codeToChar[code] = ch;
    }

    // Reconstruct tree from codeToChar map
    HuffmanNode* root = new HuffmanNode('\0', 0);
    for (const auto& pair : codeToChar) {
        HuffmanNode* curr = root;
        const std::string& code = pair.first;
        char ch = pair.second;

        for (char bit : code) {
            if (bit == '0') {
                if (!curr->left) curr->left = new HuffmanNode('\0', 0);
                curr = curr->left;
            } else {
                if (!curr->right) curr->right = new HuffmanNode('\0', 0);
                curr = curr->right;
            }
        }
        curr->ch = ch;
    }

    return root;
}

// Decompress the file
void decompressFile(const std::string& inputFile, const std::string& outputFile) {
    std::ifstream in(inputFile, std::ios::binary);
    std::ofstream out(outputFile, std::ios::binary);

    HuffmanNode* root = readCodeTable(in);

    // Read padding
    int padding = in.get();

    // Read rest of file as bitstring
    std::string bitString = "";
    char byte;
    while (in.get(byte)) {
        std::bitset<8> bits(static_cast<unsigned char>(byte));
        bitString += bits.to_string();
    }

    // Remove padding
    if (padding != 0) {
        bitString.erase(bitString.end() - padding, bitString.end());
    }

    // Decode using tree
    HuffmanNode* curr = root;
    for (char bit : bitString) {
        if (bit == '0') curr = curr->left;
        else curr = curr->right;

        if (curr->isLeaf()) {
            out.put(curr->ch);
            curr = root;
        }
    }

    in.close();
    out.close();
    freeTree(root);
}
