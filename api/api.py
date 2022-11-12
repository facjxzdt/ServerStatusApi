from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from lib.add_machine import *
from lib.jsonr import *
import uvicorn

config=read_json('config.json')
app=FastAPI()

class Machine_Info_Based(BaseModel):
    system:str
    processor:str
    system_v:str
    cpu_count:int
    cpu_count_logical:int
    mem_gb:float
    mem_mb:float
    #Machine_Number:int

class Machine_Info_Device(BaseModel):
    cpu_usage:float
    bytes_sent:str
    bytes_rcvd:str
    total_disk:float
    used_disk:float
    free_disk:float
    mem_used:float

@app.get('/')
async def root():
    return {"status": "ok"}

@app.get('/upload')
async def upload_index():
    return {"message":"这里是数据上传接口"}

@app.post('/upload/based/{machine}')
async def upload(machine,info:Machine_Info_Based,secret:str):
    if(secret==config['Password']):
        add_machine_info(machine,info.dict(),config)
    else:
        return "Illegal key"

@app.post('/upload/device/{machine}')
async def upload_device(machine,info:Machine_Info_Device,secret:str):
    if(secret==config['Password']):
        add_machine_device(machine,info.dict(),config)
    else:
        return 'Illegal key'

@app.get('/info/based/{machine}')
async def return_based_info(machine,secret):
    try:
        if(str(secret)==config['Password']):
            return JSONResponse(read_json(f'data/{machine}/based_info.json'))
        else:
            return 'Key error'
    except:
        return 'Error'

@app.get('/info/device/{machine}')
async def return_device_info(machine,secret):
    try:
        if(str(secret)==config['Password']):
            return JSONResponse(read_json(f'data/{machine}/device_info.json'))
        else:
            return 'Key error'
    except:
        return 'Error'

if __name__ == '__main__':
    uvicorn.run("api:app", host="127.0.0.1", port=8000, log_level="info")
