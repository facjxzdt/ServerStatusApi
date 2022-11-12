import requests
import time
import sys,json
import lib.jsonr
import lib.get_info
import lib.logger

info=lib.get_info.System_Info()
config=lib.jsonr.read_json('config.json')
logger=lib.logger.Logger()

based_info=json.dumps(info.return_info())

def test(url):
    try:
        requests.get(url)
        logger.info('已连接到服务器')
    except:
        logger.error('连接到服务器失败')
        sys.exit()

def upload_info(url,info_based:dict,secret:str):
    url=url+'/upload/based/{}'.format(config['Name'])
    res=requests.post(url+f'?secret={secret}',data=based_info)

def upload_device(url,secret:str):
    url=url+'/upload/device/{}'.format(config['Name'])
    device_info=json.dumps(info.return_info('device'))
    res=requests.post(url+f'?secret={secret}',data=device_info)

if __name__=='__main__':
    test(config["Server"])
    upload_info(config['Server'],based_info,config['Password'])
    while True:
        upload_device(config['Server'],config['Password'])
        time.sleep(config['Time'])