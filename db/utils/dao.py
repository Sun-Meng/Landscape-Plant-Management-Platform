#请实现链接操作
import abc
import pymssql
class dao(metaclass=abc.ABCMeta):  # 接口
    @abc.abstractmethod
    def get_conn(self):
        pass
    
    @abc.abstractmethod
    def close_conn(self):
        pass

class base_dao(dao):  # 具体实现类
    _conn = None
    
    def get_conn(self):
        self._conn = pymssql.connect(server='localhost', database="LPIM",autocommit=True) # 孙孟 DESKTOP-MTS8V3O ；海森 LAPTOP-6QSRVR56 ；
        return self._conn
    
    def close_conn(self):
        self._conn.close()