#ifndef HUFFMAN_TREE_HPP
#define HUFFMAN_TREE_HPP

#include <unordered_map>
#include <queue> // for priority queue
#include <string>

struct HuffmanNode {
    // attributes
    char ch;
    int freq;
    HuffmanNode* left;
    HuffmanNode* right;

    // Constructor
    HuffmanNode(char character, int frequency): ch(character), freq(frequency), left(nullptr), right(nullptr) {}

    // Helper to detect leaf node
    bool isLeaf() const {
        return !left && !right;
    }
};

// Comparator for priority queue
struct Compare {
    bool operator()(HuffmanNode* a, HuffmanNode* b) {
        return a->freq > b->freq;
    }
};

// methods to buikd tree, generate huffman codes and free the tree
HuffmanNode* buildHuffmanTree(const std::unordered_map<char, int>& freqTable);
void generateCodes(HuffmanNode* root, const std::string& code,std::unordered_map<char, std::string>& huffCodes);
void freeTree(HuffmanNode* root);

#endif // HUFFMAN_TREE_HPP
