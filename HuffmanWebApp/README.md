
## HuffmanWebApp

**HuffmanWebApp** is a simple and user-friendly **web interface** built with **Flask** to demonstrate **file compression and decompression using Huffman Coding**. It wraps a compiled C++ Huffman compressor (`huffman_compressor.exe`) and provides a way to upload files, compress them, and download the results — all from the browser.

---

##  Features

- Upload `.txt` files to compress or decompress.
- Uses a backend Huffman coding algorithm implemented in **C++**.
- Clean Flask web interface.
- Auto-downloads the compressed or decompressed file.
- Automatically handles file extensions to avoid redundant `.txt.out.txt` issues.
- Organizes files into `uploads/` and `output/` folders.

---

##  Project Structure

```

HuffmanWebApp/
├── app.py                      # Main Flask app
├── huffman\_compressor.exe      # Compiled C++ Huffman compressor
├── templates/
│   └── index.html              # Upload form (HTML)
├── static/
│   └── style.css               # Custom styling
├── uploads/                    # Uploaded files go here
│   └── sample.txt
├── output/                     # Output files are saved here
│   └── sample.huff
├── test/                       # Optional test files
│   └── sample.txt
└── README.md                   # You're here!

````

---

##  How to Run the Web App

###  Prerequisites

- Python 3.8+
- `Flask` library
- Windows OS (or WSL/Linux with adapted binary)

###  Step-by-step Setup

1. **Install Flask** (if not already):

   ```bash
   pip install flask
````

2. **Place your `huffman_compressor.exe`** in the project root.

3. **Run the Flask server**:

   ```bash
   python app.py
   ```

4. Open your browser and go to:

   ```
   http://127.0.0.1:5000/
   ```

---

## Supported Actions

### 🔹 Compress

* Upload a `.txt` file
* Click **"Compress"**
* Downloads: `filename.huff`

### 🔹 Decompress

* Upload a `.huff` or `.out` file
* Click **"Decompress"**
* Downloads: `filename.txt`

---

##  How It Works

* `app.py` handles file uploads, determines whether to compress or decompress.
* It calls `huffman_compressor.exe` using `subprocess.run(...)`.
* Output file is sent back to the user via `send_file(...)`.

---

##  Notes

* Make sure the `.exe` supports CLI arguments:
  `-c input.txt output.huff` for compression
  `-d input.huff output.txt` for decompression

* The app automatically sanitizes filenames and manages output extensions.

---

##  To Do (Optional Improvements)

* Add progress bars or compression stats.
* Use UUIDs or timestamps to prevent filename clashes.
* Deploy to a remote server or containerize with Docker.

---

## Author

**Dasari Veera Venkata Abhinav Teja**
B.Tech, Computer Science & Engineering
IIT Kharagpur
[GitHub](https://github.com/abhinavteja2005)

---

##  License

This project is licensed for educational and personal use. Feel free to adapt it with attribution.

```

