from audioop import add
from fastapi import FastAPI, Request, Query
import os
import configparser
from datetime import *
from typing import Optional
import uvicorn
dateToday = datetime.date(datetime.now()).strftime("%Y%m%d")
config = configparser.ConfigParser()
pwd=os.getcwd()
#Logging
def logwriterfunc(msg):
    os.makedirs(pwd+"/logs/", exist_ok=True)
    logWriter = open (pwd+"/logs/"+dateToday+"_robocoapi.log", "a+")
    logWriter.write(datetime.time(datetime.now()).strftime("[%H:%M:%S]")+" "+msg+"\n")
    logWriter.close()

#Check if config file exists
if (os.path.isfile(pwd+"/config.ini")):
    config.read(pwd+'/config.ini')

else:
    print("ERROR: NO CONFIG FILE! Exiting...")
    logwriterfunc("[ERROR] - Started without config File, please rename TEMPLATEconfig.ini to config.ini and fill the parameters.\n")
    quit()

checkerdir = config['MAIN']['checkerdir']
dldir = config['MAIN']['dldir']
app = FastAPI(
    title="Roboco API",
    description="A simple API for feeding my Archiver.",
    version="0.0.1"
)

@app.on_event("startup")
async def startup_event():
    logwriterfunc("[INFO] - Started with config File, harobo-!\n")

@app.on_event("shutdown")
async def shutdown_event():
    logwriterfunc("[INFO] - Shutting down...otsurobo...\n")

@app.get('/', tags=['main'])
async def root():
  return {'message':'Roboco API Online!'}

@app.get('/checker/list', tags=['checker'])
def checkerlist():
    #with open("/opt/archiving/ytdlppython/check_batch.txt") as check_batch_file:
    with open("/opt/TESTING/roboco-api_fastapi/check_batch.txt") as check_batch_file:
        check_batch= check_batch_file.readlines()
        check_batch_result= [line.strip() for line in check_batch]
        return {'result:':check_batch_result}

@app.post('/checker/add/', tags=['checker'])
async def checklistadd(url: str):
    #with open("/opt/archiving/ytdlppython/check_batch.txt") as checkbatchfile:
    with open("/opt/TESTING/roboco-api_fastapi/check_batch.txt") as checkbatchfile:
        dupecheckstring= checkbatchfile.read()
        checkbatchfile.close()
    if url in dupecheckstring:
        return "WARN URL already in check_batch. File not edited."
    else:
        #checkBatchAdd = open ("/opt/archiving/ytdlppython/check_batch.txt", "a+")
        checkBatchAdd = open ("/opt/TESTING/roboco-api_fastapi/check_batch.txt", "a+")
        checkBatchAdd.write(url+"\n")
        checkBatchAdd.close()
        return "Added "+url+" to checker_batch"

@app.post('/checker/bulkadd/', tags=['checker'])
async def checklistadd(url: list[str] = Query(None)):
    dupelinklist = []
    addedlinklist = []
    for link in url:
        #with open("/opt/archiving/ytdlppython/check_batch.txt") as checkbatchfile:
        with open("/opt/TESTING/roboco-api_fastapi/check_batch.txt") as checkbatchfile:
            dupecheckstring= checkbatchfile.read()
            checkbatchfile.close()
        if link in dupecheckstring:
            dupelinklist.append(link)
        else:
            #checkBatchAdd = open ("/opt/archiving/ytdlppython/check_batch.txt", "a+")
            checkBatchAdd = open ("/opt/TESTING/roboco-api_fastapi/check_batch.txt", "a+")
            checkBatchAdd.write(link+"\n")
            checkBatchAdd.close()
            addedlinklist.append(link)
    return {'dupe':dupelinklist, 'added':addedlinklist}

@app.get('/dl/list', tags=['dl'])
def dllist():
    #with open("/opt/archiving/ytdlppython/dl_batch.txt") as dl_batch_file:
    with open("/opt/TESTING/roboco-api_fastapi/dl_batch.txt") as dl_batch_file:
        dl_batch= dl_batch_file.readlines()
        dl_batch_result= [line.strip() for line in dl_batch]
        return {'result:':dl_batch_result}

@app.post('/dl/add', tags=['dl'])
def dllistadd(url: str):
    #with open("/opt/archiving/ytdlppython/check_batch.txt") as dlbatchfile:
    with open("/opt/TESTING/roboco-api_fastapi/dl_batch.txt") as dlbatchfile:
        dupecheckstring= dlbatchfile.read()
        dlbatchfile.close()
    if url in dupecheckstring:
        return "WARN URL already in check_batch. File not edited."
    else:
        dlBatchAdd = open ("/opt/TESTING/roboco-api_fastapi/dl_batch.txt", "a+")
        dlBatchAdd.write(url+"\n")
        dlBatchAdd.close()
        return "Added "+url+" to dl_batch"

@app.post('/dl/bulkadd/', tags=['dl'])
async def dllistadd(url: list[str] = Query(None)):
    dupelinklist = []
    addedlinklist = []
    for link in url:
        #with open("/opt/archiving/ytdlppython/dl_batch.txt") as dlbatchfile:
        with open("/opt/TESTING/roboco-api_fastapi/dl_batch.txt") as dlbatchfile:
            dupecheckstring= dlbatchfile.read()
            dlbatchfile.close()
        if link in dupecheckstring:
            dupelinklist.append(link)
        else:
            #checkBatchAdd = open ("/opt/archiving/ytdlppython/dl_batch.txt", "a+")
            dlBatchAdd = open ("/opt/TESTING/roboco-api_fastapi/dl_batch.txt", "a+")
            dlBatchAdd.write(link+"\n")
            dlBatchAdd.close()
            addedlinklist.append(link)
    return {'dupe':dupelinklist, 'added':addedlinklist}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5069)