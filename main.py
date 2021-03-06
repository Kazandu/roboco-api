from flask import Flask, jsonify, request
from waitress import serve
app = Flask(__name__)

@app.route('/')
def index():
  return 'Roboco API Online!'
  
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
    with open("/opt/archiving/ytdlppython/check_batch.txt") as checkbatchfile:
        dupecheckstring= checkbatchfile.read()
        checkbatchfile.close()
    if data in dupecheckstring:
        return "WARN URL already in check_batch. File not edited."
    else:
        checkBatchAdd = open ("/opt/archiving/ytdlppython/check_batch.txt", "a+")
        checkBatchAdd.write(data+"\n")
        checkBatchAdd.close()
        return "Added "+data+" to checker_batch"

@app.get('/dl/list')
def dllist():
    with open("/opt/archiving/ytdlppython/dl_batch.txt") as dl_batch_file:
        dl_batch= dl_batch_file.readlines()
        dl_batch_result= [line.strip() for line in dl_batch]
        return jsonify(dl_batch_result)

@app.get('/dl/add')
def dllistadd():
    data = request.args.get("url")
    with open("/opt/archiving/ytdlppython/check_batch.txt") as dlbatchfile:
        dupecheckstring= dlbatchfile.read()
        dlbatchfile.close()
    if data in dupecheckstring:
        return "WARN URL already in check_batch. File not edited."
    else:
        dlBatchAdd = open ("/opt/archiving/ytdlppython/dl_batch.txt", "a+")
        dlBatchAdd.write(data+"\n")
        dlBatchAdd.close()
        return "Added "+data+" to dl_batch"

if __name__ == "__main__":
    serve(app, host="127.0.0.1", port=5069)