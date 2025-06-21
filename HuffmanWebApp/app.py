import os
import subprocess
from flask import Flask, request, render_template, send_file, redirect, url_for, flash
from werkzeug.utils import secure_filename # for proper filenaming

app = Flask(__name__)
app.secret_key = "secret" 

# the uploads and output will be stored in the following directories
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
            filename = secure_filename(file.filename)  # sanitizes the filename
            base, ext = os.path.splitext(filename)

            input_path = os.path.join(UPLOAD_FOLDER, filename)

            # Correct output name
            if action == "compress":
                output_name = base + ".huff"   # or ".out" if you prefer
            else:  # decompress
                # if decompressing something like sample.huff
                if ext == ".huff" or ext == ".out":
                    output_name = base + ".txt"
                else:
                    output_name = filename + ".decompressed.txt"  # fallback

            output_path = os.path.join(OUTPUT_FOLDER, output_name)
            file.save(input_path)

            compressor_path = os.path.join(os.path.dirname(__file__), "huffman_compressor.exe")

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