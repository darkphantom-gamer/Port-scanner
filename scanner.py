import re
from flask import Flask, request, jsonify, render_template, Response
import subprocess
import shutil

app = Flask(__name__)

def check_and_install_nmap():
    """Check if Nmap is installed and install it if not."""
    if shutil.which("nmap") is None:
        try:
            print("Nmap not found. Installing Nmap...")
            subprocess.run(
                ["sudo", "apt-get", "install", "-y", "nmap"],  # For Linux
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        except Exception as e:
            return str(e)
    return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()
    target = data.get('target')

    if not target:
        return jsonify({"error": "Target is required"}), 400

    def stream_output():
        process = subprocess.Popen(
            ["nmap", "--stats-every", "1s", target],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        content = ""
        while True:
            line = process.stdout.readline()
            if not line:
                break

            # Check for progress percentage in the output
            match = re.search(r"(\d+)\.\d+% done", line.strip())
            if match:
                percent = float(match.group(1))
                yield f"data:{percent}\n"

            # Capture the full output
            content += line

        # Once the scan is complete, send the final output
        yield f"data:100\n"
        yield f"data:{content}\n"

        process.stdout.close()
        process.wait()

    return Response(stream_output(), mimetype='text/plain')

if __name__ == '__main__':
    nmap_error = check_and_install_nmap()
    if nmap_error:
        print(f"Error installing Nmap: {nmap_error}")
    else:
        print("Nmap is installed and ready to use.")
    app.run(host="0.0.0.0", port=1000)
