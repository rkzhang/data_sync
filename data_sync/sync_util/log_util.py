#-*-coding:UTF-8-*-
'''
Created on 2014Äê12ÔÂ24ÈÕ
@author: zhangr01
'''
import logging.config

logging.config.fileConfig('../logger.ini')

app_log = logging.getLogger("app")