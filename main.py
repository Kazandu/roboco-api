from flask import Flask, jsonify, request
from waitress import serve
app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.get('/health')
def healthcheck():
  return 'OK'

@app.get('/checker/list')
def checkerlist():
    with open("/opt/archiving/ytdlppython/check_batch.txt") as check_batch_file:
        check_batch= check_batch_file.readlines()
        check_batch_result= [line.strip() for line in check_batch]
        return jsonify(check_batch_result)

@app.get('/checker/add')
def checklistadd():
    data = request.args.get("url")
    checkBatchAdd = open ("/opt/archiving/ytdlppython/TEST_check_batch.txt", "a+")
    checkBatchAdd.write(data+"\n")
    checkBatchAdd.close()
    return "Abgegriffene URL ="+data

if __name__ == "__main__":
    serve(app, host="127.0.0.1", port=5069)