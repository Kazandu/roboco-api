from flask import Flask, jsonify
from waitress import serve
app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/health')
def say_hello():
  return 'Hello from Server'

@app.route('/checker/list')
def checkerlist():
    with open("/opt/archiving/ytdlppython/check_batch.txt") as check_batch_file:
        check_batch_result= check_batch_file.readlines()
        return jsonify(check_batch_result)


if __name__ == "__main__":
    serve(app, host="127.0.0.1", port=5069)