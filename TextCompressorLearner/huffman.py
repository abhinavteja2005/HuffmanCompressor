import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCode:
    def __init__(self, symbols, freqs):
        self.codes = {}
        self.root = self.build_tree(symbols, freqs)
        self.generate_codes(self.root, "")

    def build_tree(self, symbols, freqs):
        heap = [Node(char, freq) for char, freq in zip(symbols, freqs)]
        heapq.heapify(heap)

        while len(heap) > 1:
            l = heapq.heappop(heap)
            r = heapq.heappop(heap)
            merged = Node(None, l.freq + r.freq)
            merged.left = l
            merged.right = r
            heapq.heappush(heap, merged)

        return heap[0] if heap else None

    def generate_codes(self, node, code):
        if not node:
            return
        if node.char is not None:
            self.codes[node.char] = code
        self.generate_codes(node.left, code + "0")
        self.generate_codes(node.right, code + "1")

    def get_code(self, char):
        return self.codes.get(char, "")

    def encode(self, text):
        return ''.join(self.codes.get(ch, '') for ch in text)

    def decode(self, binary):
        result = ''
        node = self.root
        for bit in binary:
            node = node.left if bit == '0' else node.right
            if node.char is not None:
                result += node.char
                node = self.root
        return result
