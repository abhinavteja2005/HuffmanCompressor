---
## Huffman File Compressor

This project is a **file compression and decompression tool** based on the **Huffman Coding** algorithm, implemented in **C++**.

Huffman Coding is a popular lossless compression technique that assigns shorter binary codes to more frequent characters, reducing the total file size.

---

## Features

- Compress any plain text file using Huffman encoding.
- Decompress encoded files back to their original content.
- Clean and modular code (split into headers and source files).
- Easily extendable and readable.
- Built using standard C++17 — no external libraries required.

---

## 📁 Project Structure

```
```bash
File Compressor/
├── main.cpp                 # Entry point
├── include/
│   ├── encoder.hpp
│   ├── decoder.hpp
│   └── huffman_tree.hpp
├── src/
│   ├── encoder.cpp
│   ├── decoder.cpp
│   └── huffman_tree.cpp
├── .vscode/
│   └── tasks.json           # Build configuration for VS Code
└── huffman_compressor.exe   # Output binary (after build)

````
---

## How to Build & Run

### Using VS Code (Recommended)

1. Open the `File Compressor` folder in **Visual Studio Code**.
2. Press `Ctrl + Shift + B` to **build** the project.
3. This creates an executable named:  
   `huffman_compressor` (or `.exe` on Windows).
4. To run the program, use the integrated terminal:

```bash
./huffman_compressor
````

Or on Windows:

```cmd
huffman_compressor.exe
```

---

##  Manual Build (without VS Code)

If you're using the terminal directly:

```bash
g++ -std=c++17 -O2 -Iinclude main.cpp src/huffman_tree.cpp src/encoder.cpp src/decoder.cpp -o huffman_compressor
```

Then run it:

```bash
./huffman_compressor
```

---

##  Usage Notes

* Input/output methods (like file reading/writing) can be implemented inside `main.cpp` or `encoder.cpp/decoder.cpp`.
* Make sure the input file exists before running compression.
* You can enhance the program by adding a GUI, drag-and-drop, or web interface.

---

##  License

This project is licensed for educational and personal use. Attribution appreciated.

---

##  Author

**Dasari Abhinav Teja**
IIT Kharagpur, CSE
[GitHub](https://github.com/abhinavteja2005)




