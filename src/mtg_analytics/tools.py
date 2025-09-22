import datetime
from loguru import logger
from pathlib import Path
import os

def generate_log_file_name(prefix:str) -> str:
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    return f'{prefix}_{suffix}.log'

def begin_logging(prefix:str, folder_name:str=datetime.datetime.now().strftime("%y%m%d"))->int:
    logdir = f'{Path(__file__).parent.parent.parent}/logs/{folder_name}'
    os.makedirs(logdir, exist_ok=True)
    return logger.add(logdir + "/" + prefix + "_{time}.log") # returns int of sink handle


def end_logging():
    logger.remove()



if __name__=="__main__":
    logger.debug("here")
  
    