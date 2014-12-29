#-*-coding:UTF-8-*-
'''
Created on 2014年12月18日

@author: zhangr01
'''
from sync_util.conn_util import redis_conn, SYNC_QUEUE, getConn, getCur
import threading
from sync_util.log_util import app_log


def achieveRecord() :
    rec = redis_conn.rpop(SYNC_QUEUE)
    while rec :
        yield rec
        rec = redis_conn.rpop(SYNC_QUEUE)
        
def processRecord(rec) :
    with getConn() as conn :
        with getCur(conn) as cur :
            obj = eval(rec)
            cur.execute("select * from %s where %s = '%s'" % (obj['tableName'], obj['keyName'], obj['keyValue']))    
                
            for row in cur.fetchall():  
                app_log.info(row)

'''
def consumerProcess():
    rec = redis_conn.rpop(SYNC_QUEUE)
    while rec :
        with getConn() as conn :
            with getCur(conn) as cur :
                obj = eval(rec)
                cur.execute("select * from %s where %s = '%s'" % (obj['tableName'], obj['keyName'], obj['keyValue']))    
                    
                for row in cur.fetchall():  
                    app_log.info(row)
                  
        rec = redis_conn.rpop(SYNC_QUEUE)
'''
                        
class ConsumerThread(threading.Thread) :
    def __init__(self) : 
        threading.Thread.__init__(self)
        self.daemon = True #设置daemon标志会使解析器在主程序退出后立即退出
        
    def run(self) : 
        for rec in achieveRecord() :
            processRecord(rec)
            
        
        