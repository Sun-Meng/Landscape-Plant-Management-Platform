import abc

class careJob_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self,CareJob):
        pass
    @abc.abstractmethod
    def update(self,CareJob) :
        pass
    @abc.abstractmethod
    def delete(self,CareJob):
        pass
    @abc.abstractmethod
    def select(self,sql) :
        pass

class careWorker_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self,CareWorker):
        pass
    @abc.abstractmethod
    def update(self,CareWorker) :
        pass
    @abc.abstractmethod
    def delete(self,CareWorker):
        pass
    @abc.abstractmethod
    def select(self,sql) :
        pass

class plant_Family_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self,PlantFamily):
        pass
    @abc.abstractmethod
    def update(self,PlantFamily) :
        pass
    @abc.abstractmethod
    def delete(self,PlantFamily):
        pass
    @abc.abstractmethod
    def select(self,sql) :
        pass

class plant_Genus_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self,PlantGenus):
        pass
    @abc.abstractmethod
    def update(self,PlantGenus) :
        pass
    @abc.abstractmethod
    def delete(self,PlantGenus):
        pass
    @abc.abstractmethod
    def select(self,sql) :
        pass

class plant_Species_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self,PlantSpecies):
        pass
    @abc.abstractmethod
    def update(self,PlantSpecies) :
        pass
    @abc.abstractmethod
    def delete(self,PlantSpecies):
        pass
    @abc.abstractmethod
    def select(self,sql) :
        pass

class plant_Zone_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self,PlantZone):
        pass
    @abc.abstractmethod
    def update(self,PlantZone) :
        pass
    @abc.abstractmethod
    def delete(self,PlantZone):
        pass
    @abc.abstractmethod
    def select(self,sql) :
        pass


class user_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self,User):
        pass
    @abc.abstractmethod
    def update(self,User) :
        pass
    @abc.abstractmethod
    def delete(self,User):
        pass
    @abc.abstractmethod
    def select(self,sql) :
        pass
    
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