#请实现链接操作
import abc
import pymssql
class dao(metaclass=abc.ABCMeta):#接口@abc.abstractmethod#抽象方法
    def get_conn(c1s):
        pass
    def close_conn(c1s):    
        pass
class base_dao(dao):#具体实现类
    _conn = None
    def get_conn(c1s):
        cls._conn = pymssql.connect(server="127.0.0.1"，database="education")
        return cls._conn
    def close_conn(c1s,conn)
        conn.close()