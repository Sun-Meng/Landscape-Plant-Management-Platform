#请实现链接操作
import abc
import pymssql
class dao(metaclass=abc.ABCMeta):#接口@abc.abstractmethod#抽象方法
    def get_conn(cls):
        pass
    def close_conn(cls):    
        pass
class base_dao(dao):#具体实现类
    _conn = None
    def get_conn(cls):
        cls._conn = pymssql.connect(server="127.0.0.1",database="LPIM")
        return cls._conn
    def close_conn(cls,conn):
        conn.close()