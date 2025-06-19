#ifndef ENCODER_HPP
#define ENCODER_HPP

#include <string>
#include <unordered_map>
#include "huffman_tree.hpp"

// Count frequency of characters in input file
std::unordered_map<char, int> buildFrequencyTable(const std::string& inputFile);

// Encode the input file and write compressed output
void compressFile(const std::string& inputFile, const std::string& outputFile);

#endif // ENCODER_HPP
