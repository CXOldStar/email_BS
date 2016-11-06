# -*- coding: utf-8 -*-
import os
DEBUG = False
DIRNAME = os.path.dirname(__file__)  # return the dir path of settings_config.py
STATIC_PATH = os.path.join(DIRNAME, 'static')  # dir of static
TEMPLATE_PATH = os.path.join(DIRNAME, 'template')  # dir of template

import logging
import sys
# log linked to the standard error stream
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)-8s - %(message)s',
                    datefmt='%d/%m/%Y %Hh%Mm%Ss')

COOKIE_SECRET = 'L8LwECiNRxq2N0N2eGxx9MZlrpmuMEimlydNX/'

if __name__ == '__main__':
    name = os.path.dirname(__file__)
    print('dir:', name)
