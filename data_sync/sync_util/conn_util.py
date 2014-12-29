#-*-coding:UTF-8-*-
'''
Created on 2014Äê12ÔÂ24ÈÕ

@author: zhangr01
'''
import redis
import MySQLdb
from DBUtils.PooledDB import PooledDB
from MySQLdb.cursors import DictCursor
from sync_util.config_util import cfg
from contextlib import contextmanager

redis_conn = redis.Redis(host='127.0.0.1', port=6379, db=0) 

SYNC_QUEUE = 'wedding.sync.queue'

host = cfg.get('db_conn', 'host')
port = cfg.getint('db_conn', 'port')
user = cfg.get('db_conn', 'user')
passwd = cfg.get('db_conn', 'passwd') 
db = cfg.get('db_conn', 'db')  
use_unicode = cfg.getboolean('db_conn', 'use_unicode')
charset = cfg.get('db_conn', 'charset')

print host, port, user, passwd, db, use_unicode, charset

conn_pool = PooledDB(creator=MySQLdb, mincached=1 , maxcached=20 ,
                              host=host , port=port , user=user, passwd=passwd,
                              db=db ,use_unicode=use_unicode,charset=charset,cursorclass=DictCursor)


def getDbConn() : 
    return conn_pool.connection()

@contextmanager
def getConn() :
    conn= conn_pool.connection()   
    yield conn
    conn.close()
    
    
@contextmanager
def getCur(conn) : 
    cur = conn.cursor()
    yield cur
    cur.close()

'''
db_conn= MySQLdb.connect(
        host='115.29.245.7',
        port = 3306,
        user='bridal',
        passwd='bridal',
        db ='wedding',
        charset="utf8"
        )
'''