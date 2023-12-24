class CareJob(object):
    def __init__(self, JobID,WorkerID,Name, Date, Location,RegularJob,Result,create_time,modified_time):
        self.__JobID = JobID
        self.__WorkerID = WorkerID
        self.__Name = Name
        self.__Date = Date
        self.__Location = Location
        self.__RegularJob=RegularJob
        self.__Result=Result
        self.__create_time = create_time
        self.__modified_time=modified_time


class CareWorker(object):
    def __init__(self, ID, Name, Sex, Birth, Tel,create_time,modified_time):
        self.__ID = ID
        self.__Name = Name
        self.__Sex = Sex
        self.__Birth = Birth
        self.__Tel = Tel
        self.__create_time = create_time
        self.__modified_time=modified_time

    

class PlantFamily(object):
     def __init__(self, id,name,info):
        self.__id=id
        self.__name=name
        self.__info = info


class PlantGenus(object):
     def __init__(self, id,name,info):
        self.__id=id
        self.__name=name
        self.__info = info


class PlantSpecies(object):
    def __init__(self, id,name,info):
        self.__id=id
        self.__name=name
        self.__info = info
        

class PlantZone(object):
    def __init__(self,ZoneID, Prov, City, County, create_time,modified_time):
        self.__ZoneID = ZoneID
        self.__Prov = Prov
        self.__City = City
        self.__County = County
        self.__create_time = create_time
        self.__modified_time=modified_time
