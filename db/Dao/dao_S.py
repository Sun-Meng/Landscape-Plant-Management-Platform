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