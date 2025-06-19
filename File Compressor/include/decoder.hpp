#ifndef DECODER_HPP
#define DECODER_HPP

#include <string>
#include <unordered_map>
#include "huffman_tree.hpp"

// Decode the compressed .huff file to original file
void decompressFile(const std::string& inputFile, const std::string& outputFile);

#endif // DECODER_HPP
