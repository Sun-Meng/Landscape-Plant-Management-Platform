class CareJob(object):
    def __init__(self, JobID,WorkerID,Name, Date, Location,RegularJob,Result):
        self.__JobID = JobID
        self.__WorkerID = WorkerID
        self.__Name = Name
        self.__Date = Date
        self.__Location = Location
        self.__RegularJob=RegularJob
        self.__Result=Result


class CareWorker(object):
    def __init__(self, ID, Name, Sex, Birth, Tel):
        self.__ID = ID
        self.__Name = Name
        self.__Sex = Sex
        self.__Birth = Birth
        self.__Tel = Tel

    def get_ID(self):
        return self.__ID

    def get_Name(self):
        return self.__Name

    def get_Sex(self):
        return self.__Sex
    
    def get_Age(self):
        return self.__Age
    
    def get_Tel(self):
        return self.__Tel
    

class PlantFamily(object):
     def __init__(self, PlantID, id,name,info):
        self.__PlantID = PlantID
        self.__id=id
        self.__name=name
        self.__info = info


class PlantGenus(object):
     def __init__(self, PlantID, id,name,info):
        self.__PlantID = PlantID
        self.__id=id
        self.__name=name
        self.__info = info


class PlantSpecies(object):
    def __init__(self, PlantID, id,name,info):
        self.__PlantID = PlantID
        self.__id=id
        self.__name=name
        self.__info = info
        

class PlantZone(object):
    def __init__(self, PlantID,ZoneID, Prov, City, County, create_time,modified_time):
        self.__PlantID = PlantID
        self.__ZoneID = ZoneID
        self.__Prov = Prov
        self.__City = City
        self.__County = County
        self.__create_time = create_time
        self.__modified_time=modified_time
