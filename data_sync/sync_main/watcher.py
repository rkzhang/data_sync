#-*-coding:UTF-8-*-
'''
@author: zhangr01
'''
import time
import threading
from sync_util.conn_util import redis_conn, SYNC_QUEUE, getConn, getCur

def watcherProcess():
    while True : 
        try :            
            with getConn() as conn :
                with getCur(conn) as cur :
                    cur.execute("select * from wd_data_sync where Err_Info is null order by id limit 0, 100")    
                
                    results = cur.fetchall()
                    
                    if len(results) == 0 :
                        time.sleep(5)
                        continue
                    
                    for row in results:  
                        record = {}
                        record['id'] = row['id']
                        record['tableName'] = row['Table_Name']
                        record['keyName'] = row['Key_Name']
                        record['keyValue'] = row['Key_Value']
                        record['optType'] = row['Opt_Type']
                        record['errInfo'] = row['Err_Info']
                                        
                        cur.execute("delete from wd_data_sync where id=%d" % record['id'])
                        redis_conn.lpush(SYNC_QUEUE, record)
                        
        except Exception, e :
            print e


class WatcherThread(threading.Thread) :
    def __init__(self) : 
        threading.Thread.__init__(self)
        self.daemon = True #设置daemon标志会使解析器在主程序退出后立即退出
        
    def run(self) : 
        watcherProcess()



