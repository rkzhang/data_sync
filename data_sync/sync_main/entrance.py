#-*-coding:UTF-8-*-
'''
Created on 2014Äê12ÔÂ24ÈÕ
@author: zhangr01
'''
from sync_main.watcher import WatcherThread
from sync_main.data_consumer import ConsumerThread
import time

t_watcher = WatcherThread();
t_watcher.start()

for i in range(5) :
    t_consumer = ConsumerThread();
    t_consumer.start()

while True : 
    time.sleep(10)