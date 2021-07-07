from flask import Flask
import os
k8s_pod = os.getenv("HOSTNAME")

app = Flask(__name__)

@app.route('/index')
def index():
    return f"Hello from Kubernetes POD {k8s_pod}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
