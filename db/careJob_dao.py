import abc
class careJob_dao(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def insert(self,CareJob):
        pass
    @abc.abstractclassmethod
    def delete(self,CareJob):
        pass
    @abc.abstractclassmethod
    def update(self,CareJob):
        pass
    @abc.abstractclassmethod
    def select(self,CareJob):
        pass