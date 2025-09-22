#!/usr/bin/env python

import mtg_analytics.deck as deck
import mtg_analytics.main as main
import mtg_analytics.tools as tools
from loguru import logger
import os
from glob import glob
from pathlib import Path
import shutil



def test_logging():
    test_name = "test"
    tools.begin_logging(test_name, test_name)
    logger.debug("blorb")
    log_file = glob(f'{Path(__file__).parent.parent}/logs/{test_name}/{test_name}*.log')[0]

    with open(log_file, 'r') as file:
        contents = file.read()
        print("beep")
        print(contents)
        assert contents.endswith("blorb\n")
    
    tools.end_logging()
    shutil.rmtree(f'{Path(__file__).parent.parent}/logs/{test_name}/')

if __name__=="__main__":
    test_logging()

