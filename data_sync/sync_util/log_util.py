#-*-coding:UTF-8-*-
'''
Created on 2014��12��24��
@author: zhangr01
'''
import logging.config

logging.config.fileConfig('../logger.ini')

app_log = logging.getLogger("app")