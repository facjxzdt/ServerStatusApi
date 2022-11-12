import os,json
from lib.jsonr import *
import logger
loggers=lib.loggers.Logger()

def mkdir(path):
    folder=os.path.exists(path)
    if not folder:
        os.makedirs(path)
        return 1

def add_machine_info(machine:str,info_based:dict,config:dict):
    mkdir(f'./data/{machine}')
    with open(f'./data/{machine}/based_info.json','w') as f:
        json.dump(info_based,f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',',':'))
        loggers.info(f'添加{machine}机器信息成功')

def add_machine_device(machine:str,info_device:dict,config:dict):
    try:
        with open(f'./data/{machine}/device_info.json','w') as f:
            json.dump(info_device,f,ensure_ascii=False,sort_keys=True,indent=4,separators=(',',':'))
            loggers.info(f'更新{machine}机器硬件信息成功')
    except:
        loggers.error(f'更新{machine}信息失败，请检查是否已经添加该机器')