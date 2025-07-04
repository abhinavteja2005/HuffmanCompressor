import os
import subprocess
from flask import Flask, request, render_template, send_file, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "secret"

# Directories for uploads and outputs
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        action = request.form.get("action")

        if file and action in ("compress", "decompress"):
            filename = secure_filename(file.filename)
            base, ext = os.path.splitext(filename)

            input_path = os.path.abspath(os.path.join(UPLOAD_FOLDER, filename))

            # Determine output filename
            if action == "compress":
                output_name = base + ".huff"
            else:
                if ext == ".huff" or ext == ".out":
                    output_name = base + ".txt"
                else:
                    output_name = filename + ".decompressed.txt"

            output_path = os.path.abspath(os.path.join(OUTPUT_FOLDER, output_name))
            file.save(input_path)

            # Path to C++ compressor executable
            compressor_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "huffman_compressor.exe"))

            # Debug info
            print("Compressor path:", compressor_path)
            print("Input path:", input_path)
            print("Output path:", output_path)

            try:
                if action == "compress":
                    subprocess.run([compressor_path, "-c", input_path, output_path], check=True)
                else:
                    subprocess.run([compressor_path, "-d", input_path, output_path], check=True)

                # Wait until output file is actually created
                if not os.path.exists(output_path):
                    flash("Error: Output file not created.")
                    return redirect(url_for("index"))

                return send_file(output_path, as_attachment=True)

            except subprocess.CalledProcessError:
                flash("Compression/Decompression failed during execution.")
                return redirect(url_for("index"))

        flash("Invalid file or action.")
        return redirect(url_for("index"))

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
