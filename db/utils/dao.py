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
        self._conn = pymssql.connect(server='DESKTOP-MTS8V3O', database="LPIM",autocommit=True)
        return self._conn
    
    def close_conn(self):
        self._conn.close()