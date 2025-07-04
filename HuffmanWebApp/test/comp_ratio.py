import os

original_size = os.path.getsize(r"C:\Users\ASUS\OneDrive\Desktop\Software Projects\HuffmanCompressor\HuffmanWebApp\test\sample.txt")
compressed_size = os.path.getsize(r"C:\Users\ASUS\OneDrive\Desktop\Software Projects\HuffmanCompressor\output\sample.huff")

compression_ratio = original_size / compressed_size
compression_percent = (1 - compressed_size / original_size) * 100

print(f"Compression Ratio: {compression_ratio:.2f}")
print(f"Size reduced by: {compression_percent:.2f}%")
