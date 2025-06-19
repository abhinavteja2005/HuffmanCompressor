# huffman.py

class Node:
    def __init__(self, info, freq):
        self.info = info          # character
        self.freq = freq          # frequency
        self.code = ""            # binary code string
        self.left = None          # left child
        self.right = None         # right child

    def is_leaf(self):
        return self.info != '\0'


class BinaryTree:
    def __init__(self):
        self.root = None

    def assign_codes(self, node=None, current_code=""):
        if node is None:
            node = self.root
        if node.is_leaf():
            node.code = current_code
            print(f"{node.info}\t{node.code}")
        else:
            if node.left:
                self.assign_codes(node.left, current_code + "0")
            if node.right:
                self.assign_codes(node.right, current_code + "1")

    def get_code(self, char, node=None):
        if node is None:
            node = self.root
        if node.is_leaf() and node.info == char:
            return node.code
        if node.left:
            code = self.get_code(char, node.left)
            if code:
                return code
        if node.right:
            code = self.get_code(char, node.right)
            if code:
                return code
        return ""

    def encode(self, text):
        encoded = ""
        for char in text:
            code = self.get_code(char)
            encoded += code
        return encoded

    def decode(self, encoded_text):
        decoded = ""
        node = self.root
        for bit in encoded_text:
            if bit == '0':
                node = node.left
            else:
                node = node.right
            if node.is_leaf():
                decoded += node.info
                node = self.root
        return decoded


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, tree):
        self.heap.append(tree)
        self.heap.sort(key=lambda t: t.root.freq)

    def remove(self):
        return self.heap.pop(0)

    def size(self):
        return len(self.heap)


class HuffmanCode:
    def __init__(self, symbols, frequencies):
        self.huffman_tree = self.build_tree(symbols, frequencies)

    def build_tree(self, symbols, frequencies):
        heap = MinHeap()
        for i in range(len(symbols)):
            node = Node(symbols[i], frequencies[i])
            tree = BinaryTree()
            tree.root = node
            heap.insert(tree)

        while heap.size() > 1:
            left_tree = heap.remove()
            right_tree = heap.remove()

            merged_node = Node('\0', left_tree.root.freq + right_tree.root.freq)
            merged_node.left = left_tree.root
            merged_node.right = right_tree.root

            new_tree = BinaryTree()
            new_tree.root = merged_node
            heap.insert(new_tree)

        final_tree = heap.remove()
        final_tree.assign_codes()
        return final_tree

    def encode(self, text):
        return self.huffman_tree.encode(text)

    def decode(self, encoded_text):
        return self.huffman_tree.decode(encoded_text)
