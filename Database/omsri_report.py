# -*- coding: utf-8 -*-
# Title           :omsri_report.py
# Description     :This will create a csv formated report of omsri application.
# Author          :Dhanasekara Pandian
# Email           :sekar5in@quehive.com
# Date            :20191210
# Version         :0.1
# Usage           :python omsri_report.py
# Notes           :This is proprietary software of QueHive Technologies Pvt Ltd.
# Python_version  :3.6

import logging

'''
MODE:

    DEBUG
    INFO
    WARNING
    ERROR
    CRITICAL

'''


logging.basicConfig(filename='omsri_report.log', datefmt='%d-%b-%y %H:%M:%S', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')