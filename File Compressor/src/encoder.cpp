#include "encoder.hpp"
#include <fstream>
#include <bitset>
#include <cstdint>
#include <iostream>

// Create frequency table from file
std::unordered_map<char, int> buildFrequencyTable(const std::string& inputFile) {
    std::unordered_map<char, int> freqTable;
    std::ifstream in(inputFile, std::ios::binary);

    char ch;
    while (in.get(ch)) {
        freqTable[ch]++;
    }

    in.close();
    return freqTable;
}

// Write metadata: tree as {char, code} pairs
void writeCodeTable(std::ofstream& out, const std::unordered_map<char, std::string>& huffCodes) {
    size_t tableSize = huffCodes.size();
    out.write(reinterpret_cast<const char*>(&tableSize), sizeof(tableSize));

    for (const auto& pair : huffCodes) {
        out.put(pair.first);
        uint8_t codeLen = pair.second.length();
        out.put(codeLen);

        std::bitset<256> bits(pair.second);
        for (int i = 0; i < (codeLen + 7) / 8; ++i) {
            char byte = 0;
            for (int b = 0; b < 8 && i * 8 + b < codeLen; ++b) {
                if (pair.second[i * 8 + b] == '1')
                    byte |= (1 << (7 - b));
            }
            out.put(byte);
        }
    }
}

// Encode actual file using Huffman codes
void compressFile(const std::string& inputFile, const std::string& outputFile) {
    std::unordered_map<char, int> freqTable = buildFrequencyTable(inputFile);
    HuffmanNode* root = buildHuffmanTree(freqTable);

    std::unordered_map<char, std::string> huffCodes;
    generateCodes(root, "", huffCodes);

    std::ifstream in(inputFile, std::ios::binary);
    std::ofstream out(outputFile, std::ios::binary);

    // Step 1: Write code table
    writeCodeTable(out, huffCodes);

    // Step 2: Encode and write binary
    std::string bitString = "";
    char ch;
    while (in.get(ch)) {
        bitString += huffCodes[ch];
    }

    // Pad with zeros if necessary
    int padding = 8 - (bitString.size() % 8);
    if (padding != 8)
        bitString.append(padding, '0');

    // Write padding info
    out.put(static_cast<char>(padding));

    // Write binary
    for (size_t i = 0; i < bitString.size(); i += 8) {
        std::bitset<8> byte(bitString.substr(i, 8));
        out.put(static_cast<char>(byte.to_ulong()));
    }

    in.close();
    out.close();
    freeTree(root);
}
