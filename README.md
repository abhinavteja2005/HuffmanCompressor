## Huffman Coding Compression Suite

This repository contains a comprehensive suite of projects that implement **Huffman Coding** for file compression across multiple platforms and interfaces. It demonstrates the same core algorithm used in different environments — command-line in C++, GUI in Python (Tkinter), and Web (Flask + HTML/CSS/JS).

## 📁 Project Structure

```

.
├── File Compressor          # C++ project for compression using Huffman coding
├── HuffmanWebApp            # Flask-based web interface for compression
├── TextCompressorLearn      # Python GUI using Tkinter for Huffman learning
└── .vscode                  # Editor settings

````

---

## 📦 Subprojects Overview

### 1. 🔧 **File Compressor (C++ CLI Tool)**

- A full implementation of Huffman coding in C++.
- Supports encoding and decoding of files.
- Built as a command-line executable `huffman_compressor.exe`.

📂 Located in: [`File Compressor/`](./File%20Compressor/)  
📖 Details in: [`File Compressor/README.md`](./File%20Compressor/README.md)

---

### 2. 🌐 **HuffmanWebApp (Flask Web App)**

- A web-based frontend to the C++ compressor using Flask.
- Lets users upload a file, compress it using the compiled `.exe`, and download the compressed result.
- Uses `HTML`, `CSS`, and optionally `JavaScript`.

📂 Located in: [`HuffmanWebApp/`](./HuffmanWebApp/)  
📖 Details in: [`HuffmanWebApp/README.md`](./HuffmanWebApp/README.md)

---

### 3. 🖥️ **TextCompressorLearn (Tkinter GUI in Python)**

- Educational GUI to visualize how Huffman Coding works.
- Allows users to enter text, view Huffman codes, and see compression results.

📂 Located in: [`TextCompressorLearn/`](./TextCompressorLearn/)  
📖 Details in: [`TextCompressorLearn/README.md`](./TextCompressorLearn/README.md)

---

##  Setup & Usage

### Prerequisites
- Python 3.11+ (for Tkinter GUI and Flask App)
- C++ compiler (to rebuild the CLI tool, if needed)
- Flask (for web app) – Install via pip:
  ```bash
  pip install flask
  ````

---  

###  How to Run Each Project

**1. File Compressor (C++)**

```bash
cd "File Compressor"
g++ -std=c++17 -Iinclude src/*.cpp -o huffman_compressor.exe
./huffman_compressor.exe
```

**2. HuffmanWebApp (Flask)**

```bash
cd HuffmanWebApp
python app.py
```

* Open in browser: `http://localhost:5000/`

**3. TextCompressorLearn (Tkinter GUI)**

```bash
cd TextCompressorLearn
python gui.py
```

---

## Customize Compression Speed (for C++ App)

To change the speed of compression (e.g., simulate slower/faster behavior), modify the `speed` variable inside the `main.cpp` file (if implemented), or introduce a delay artificially using `std::this_thread::sleep_for`.

---

## Features

*  Huffman Tree construction
*  File compression and decompression
*  Binary output `.huff` generation
*  GUI visualization of Huffman codes
*  Web-based upload and compression service
*  Integrated Python and C++ workflows

---

##  Author

**Dasari Veera Venkata Abhinav Teja**
B.Tech CSE @ IIT Kharagpur
GitHub: [@abhinavteja2005](https://github.com/abhinavteja2005)

---

##  License

This project is open-source for educational and non-commercial use.

