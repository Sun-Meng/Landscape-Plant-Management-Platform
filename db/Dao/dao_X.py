import abc

class Monitor_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self,Monitor):
        pass
    @abc.abstractmethod
    def update(self,Monitor) :
        pass
    @abc.abstractmethod
    def delete(self,Monitor):
        pass
    @abc.abstractmethod
    def select(self,sql) :
        pass

class Monitoring_Equipment_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self,Monitoring_Equipment):
        pass
    @abc.abstractmethod
    def update(self,Monitoring_Equipment) :
        pass
    @abc.abstractmethod
    def delete(self,Monitoring_Equipment):
        pass
    @abc.abstractmethod
    def select(self,sql) :
        pass
    
class Monitoring_Personnel_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self,Monitoring_Personnel):
        pass
    @abc.abstractmethod
    def update(self,Monitoring_Personnel) :
        pass
    @abc.abstractmethod
    def delete(self,Monitoring_Personnel):
        pass
    @abc.abstractmethod
    def select(self,sql) :
        pass