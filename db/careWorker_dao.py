import abc
class careWorker_dao(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def insert(self,CareWorker):
        pass
    @abc.abstractclassmethod
    def delete(self,CareWorker):
        pass
    @abc.abstractclassmethod
    def update(self,CareWorker):
        pass
    @abc.abstractclassmethod
    def select(self,CareWorker):
        pass