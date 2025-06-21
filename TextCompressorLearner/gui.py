import tkinter as tk
from tkinter import messagebox, scrolledtext
from huffman import HuffmanCode

class HuffmanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Huffman Coding - Tkinter Version")

        self.symbols = []
        self.frequencies = []
        self.huffman = None

        self.setup_ui()

    def setup_ui(self):
        # Symbol + frequency input
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=5)

        self.symbol_entry = tk.Entry(input_frame, width=10)
        self.symbol_entry.grid(row=0, column=0, padx=5)
        self.symbol_entry.insert(0, '')

        self.freq_entry = tk.Entry(input_frame, width=10)
        self.freq_entry.grid(row=0, column=1, padx=5)
        self.freq_entry.insert(0, '')

        add_btn = tk.Button(input_frame, text="Add", command=self.add_symbol)
        add_btn.grid(row=0, column=2, padx=5)

        # Encoding input
        self.encode_entry = tk.Entry(self.root, width=40)
        self.encode_entry.pack(pady=5)
        self.encode_entry.insert(0, "")

        encode_btn = tk.Button(self.root, text="Encode", command=self.encode_text)
        encode_btn.pack(pady=2)

        # Decoding input
        self.decode_entry = tk.Entry(self.root, width=40)
        self.decode_entry.pack(pady=5)
        self.decode_entry.insert(0, "")

        decode_btn = tk.Button(self.root, text="Decode", command=self.decode_text)
        decode_btn.pack(pady=2)

        # Output area
        self.output_area = scrolledtext.ScrolledText(self.root, height=15, width=60, state='normal')
        self.output_area.pack(pady=10)

    def add_symbol(self):
        symbol = self.symbol_entry.get().strip()
        freq_text = self.freq_entry.get().strip()

        if not symbol or not freq_text:
            messagebox.showwarning("Input Error", "Enter both symbol and frequency.")
            return

        try:
            freq = int(freq_text)
        except ValueError:
            messagebox.showerror("Input Error", "Frequency must be an integer.")
            return

        self.symbols.append(symbol)
        self.frequencies.append(freq)

        self.output_area.insert(tk.END, f"Added: '{symbol}' with frequency {freq}\n")
        self.symbol_entry.delete(0, tk.END)
        self.freq_entry.delete(0, tk.END)

        self.huffman = HuffmanCode(self.symbols, self.frequencies)
        self.output_area.insert(tk.END, "\nSymbol Codes:\n")
        for s in self.symbols:
            self.output_area.insert(tk.END, f"{s} -> {self.huffman.get_code(s)}\n")

    def encode_text(self):
        if not self.huffman:
            messagebox.showerror("Error", "Add symbols first.")
            return
        text = self.encode_entry.get().strip()
        result = self.huffman.encode(text)
        self.output_area.insert(tk.END, f"\nEncoded '{text}' -> {result}\n")

    def decode_text(self):
        if not self.huffman:
            messagebox.showerror("Error", "Add symbols first.")
            return
        binary = self.decode_entry.get().strip()
        result = self.huffman.decode(binary)
        self.output_area.insert(tk.END, f"\nDecoded '{binary}' -> {result}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = HuffmanApp(root)
    root.mainloop()
