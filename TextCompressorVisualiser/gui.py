# gui.py

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
)
from huffman import HuffmanCode
import sys

class HuffmanGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Huffman Coding Visualizer")
        self.symbols = []
        self.frequencies = []
        self.huffman = None

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Symbol and frequency input
        input_layout = QHBoxLayout()
        self.symbol_input = QLineEdit()
        self.symbol_input.setPlaceholderText("Symbol")
        self.freq_input = QLineEdit()
        self.freq_input.setPlaceholderText("Frequency")
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_symbol)

        input_layout.addWidget(self.symbol_input)
        input_layout.addWidget(self.freq_input)
        input_layout.addWidget(self.add_button)

        layout.addLayout(input_layout)

        # Encode/Decode input
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Enter string to encode")
        self.encode_button = QPushButton("Encode")
        self.encode_button.clicked.connect(self.encode_text)

        self.encoded_input = QLineEdit()
        self.encoded_input.setPlaceholderText("Enter binary to decode")
        self.decode_button = QPushButton("Decode")
        self.decode_button.clicked.connect(self.decode_text)

        layout.addWidget(self.text_input)
        layout.addWidget(self.encode_button)
        layout.addWidget(self.encoded_input)
        layout.addWidget(self.decode_button)

        # Output box
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        layout.addWidget(self.output_area)

        # Finalize layout
        self.setLayout(layout)

    def add_symbol(self):
        symbol = self.symbol_input.text().strip()
        freq_text = self.freq_input.text().strip()

        if not symbol or not freq_text:
            QMessageBox.warning(self, "Input Error", "Please enter both symbol and frequency.")
            return

        try:
            freq = int(freq_text)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Frequency must be an integer.")
            return

        self.symbols.append(symbol)
        self.frequencies.append(freq)
        self.output_area.append(f"Added: '{symbol}' with frequency {freq}")
        self.symbol_input.clear()
        self.freq_input.clear()

        # Rebuild Huffman Tree each time
        self.huffman = HuffmanCode(self.symbols, self.frequencies)

    def encode_text(self):
        if not self.huffman:
            QMessageBox.warning(self, "Error", "Add symbols first.")
            return
        text = self.text_input.text().strip()
        encoded = self.huffman.encode(text)
        self.output_area.append(f"\nEncoded '{text}' -> {encoded}")

    def decode_text(self):
        if not self.huffman:
            QMessageBox.warning(self, "Error", "Add symbols first.")
            return
        encoded = self.encoded_input.text().strip()
        decoded = self.huffman.decode(encoded)
        self.output_area.append(f"\nDecoded '{encoded}' -> {decoded}")


def run_gui():
    app = QApplication(sys.argv)
    window = HuffmanGUI()
    window.resize(500, 400)
    window.show()
    sys.exit(app.exec_())
