from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
  return {'message':'Roboco API Online!'}

@app.get('/checker/list')
def checkerlist():
    #with open("/opt/archiving/ytdlppython/check_batch.txt") as check_batch_file:
        #check_batch= check_batch_file.readlines()
        #check_batch_result= [line.strip() for line in check_batch]
        check_batch_result="temp_value"
        return {'result:':check_batch_result}