# main.py

from huffman import HuffmanCode
from gui import run_gui

def main():
    print("Enter number of symbols:")
    n = int(input())
    symbols = []
    frequencies = []

    for i in range(n):
        print("Enter symbol:")
        ch = input().strip()
        print("Enter frequency:")
        freq = int(input())
        symbols.append(ch)
        frequencies.append(freq)

    huffman = HuffmanCode(symbols, frequencies)

    print("\nEnter string to encode:")
    text = input().strip()
    encoded = huffman.encode(text)
    print("Encoded string:", encoded)

    print("\nEnter encoded string to decode:")
    encoded_input = input().strip()
    decoded = huffman.decode(encoded_input)
    print("Decoded string:", decoded)


if __name__ == "__main__":
    run_gui()
    main()
