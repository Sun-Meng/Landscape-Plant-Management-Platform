#基础的增删改查已有，可在pass后增加自己的操作
import abc

class IllustrationDao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, Illustration) -> bool:
        pass
    @abc.abstractmethod
    def delete(self, Illustration) -> bool:
        pass
    @abc.abstractmethod
    def update(self, Illustration) -> bool:
        pass
    @abc.abstractmethod
    def select(self, sql):
        pass

class UsageDao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, Usage) -> bool:
        pass
    @abc.abstractmethod
    def delete(self, Usage) -> bool:
        pass
    @abc.abstractmethod
    def update(self, Usage) -> bool:
        pass
    @abc.abstractmethod
    def select(self, sql):
        pass

class MedicinesDao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, Medicines) -> bool:
        pass
    @abc.abstractmethod
    def delete(self, Medicines) -> bool:
        pass
    @abc.abstractmethod
    def update(self, Medicines) -> bool:
        pass
    @abc.abstractmethod
    def select(self, sql):
        pass

class PreventDao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, Prevent) -> bool:
        pass
    @abc.abstractmethod
    def delete(self, Prevent) -> bool:
        pass
    @abc.abstractmethod
    def update(self, Prevent) -> bool:
        pass
    @abc.abstractmethod
    def select(self, sql):
        pass

class PestInfoDao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, PestInfo) -> bool:
        pass
    @abc.abstractmethod
    def delete(self, PestInfo) -> bool:
        pass
    @abc.abstractmethod
    def update(self, PestInfo) -> bool:
        pass
    @abc.abstractmethod
    def select(self, sql):
        pass

class PlantsDao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, Plants) -> bool:
        pass
    @abc.abstractmethod
    def delete(self, Plants) -> bool:
        pass
    @abc.abstractmethod
    def update(self, Plants) -> bool:
        pass
    @abc.abstractmethod
    def select(self, sql):
        pass
        
class ShootingDao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, Shooting) -> bool:
        pass
    @abc.abstractmethod
    def delete(self, Shooting) -> bool:
        pass
    @abc.abstractmethod
    def update(self, Shooting) -> bool:
        pass
    @abc.abstractmethod
    def select(self, sql):
        pass