# app.py
import os
import subprocess
from flask import Flask, request, render_template, send_file, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "secret"  # Required for flash messages

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
            filename = file.filename
            input_path = os.path.join(UPLOAD_FOLDER, filename)
            output_name = f"{filename}.out" if action == "compress" else f"{filename}.txt"
            output_path = os.path.join(OUTPUT_FOLDER, output_name)

            file.save(input_path)

            # Full path to the executable (safe for Windows)
            compressor_path = os.path.join(os.path.dirname(__file__), "huffman_compressor.exe")

            # Run the compressor with full path
            try:
                if action == "compress":
                    subprocess.run([compressor_path, "-c", input_path, output_path], check=True)
                else:
                    subprocess.run([compressor_path, "-d", input_path, output_path], check=True)
            except subprocess.CalledProcessError:
                flash("Compression/Decompression failed.")
                return redirect(url_for("index"))


            return send_file(output_path, as_attachment=True)

        flash("Invalid file or action.")
        return redirect(url_for("index"))

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)