#include "huffman_tree.hpp"
#include <iostream>

HuffmanNode* buildHuffmanTree(const std::unordered_map<char, int>& freqTable) {
    std::priority_queue<HuffmanNode*, std::vector<HuffmanNode*>, Compare> pq;

    for (const auto& pair : freqTable) {
        pq.push(new HuffmanNode(pair.first, pair.second));
    }

    while (pq.size() > 1) {
        HuffmanNode* left = pq.top(); pq.pop();
        HuffmanNode* right = pq.top(); pq.pop();

        HuffmanNode* merged = new HuffmanNode('\0', left->freq + right->freq);
        merged->left = left;
        merged->right = right;
        pq.push(merged);
    }

    return pq.top(); // Root of the Huffman Tree
}

void generateCodes(HuffmanNode* root, const std::string& code,
                   std::unordered_map<char, std::string>& huffCodes) {
    if (!root) return;

    if (root->isLeaf()) {
        huffCodes[root->ch] = code;
    }

    generateCodes(root->left, code + "0", huffCodes);
    generateCodes(root->right, code + "1", huffCodes);
}

void freeTree(HuffmanNode* root) {
    if (!root) return;
    freeTree(root->left);
    freeTree(root->right);
    delete root;
}
