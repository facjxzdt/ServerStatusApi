import json,sys,os,lib.loggers
logger=lib.loggers.Logger()

def read_json(name):
    try:
        with open(name, "r", encoding="utf-8") as f:
            load_dict = json.load(f)
            logger.info(f'读取{name}成功')
            return load_dict
    except:
        logger.error('Configuration file error!')

def fix_json(load_dict,conf,vaule,name):
    load_dict[conf] = vaule
    with open(name, "w", encoding="utf-8") as rf:
        json.dump(load_dict, rf, ensure_ascii=False, sort_keys=True, indent=4, separators=(',',':'))