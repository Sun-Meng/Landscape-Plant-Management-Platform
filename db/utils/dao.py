#请实现链接操作
import abc
import pymssql
class Dao(metaclass=abc.ABCMeta):  # 接口
    @abc.abstractmethod
    def get_conn(self):
        pass
    
    @abc.abstractmethod
    def close_conn(self):
        pass

class BaseDao(Dao):  # 具体实现类
    _conn = None
    
    def get_conn(self):
        self._conn = pymssql.connect(server="127.0.0.1", database="LPIM")
        return self._conn
    
    def close_conn(self):
        self._conn.close()