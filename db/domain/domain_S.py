class CareJob(object):
    def __init__(self, JobID,WorkerID,Name, Date, Location,Content,Result):
        self.__JobID = JobID
        self.__WorkerID = WorkerID
        self.__Name = Name
        self.__Date = Date
        self.__Location = Location
        self.__Content=Content
        self.__Result=Result
    
    def get_JobID(self):
        return self.__JobID
    
    def get_WorkerID(self):
        return self.__WorkerID
    
    def get_Name(self):
        return self.__Name
    
    def get_Date(self):
        return self.__Date
    
    def get_Location(self):
        return self.__Location
    
    def get_Content(self):
        return self.__Content
    
    def get_Result(self):
        return self.__Result


class CareWorker(object):
    def __init__(self, ID, Name, Sex, Age, Tel):
        self.__ID = ID
        self.__Name = Name
        self.__Sex = Sex
        self.__Age = Age
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
    

class Plant_Family(object):
     def __init__(self, PlantID, id,name,info):
        self.__PlantID = PlantID
        self.__id=id
        self.__name=name
        self.__name = name


class Plant_Genus(object):
     def __init__(self, PlantID, id,name,info):
        self.__PlantID = PlantID
        self.__id=id
        self.__name=name
        self.__name = name


class Plant_Species(object):
    def __init__(self, PlantID, id,name,info):
        self.__PlantID = PlantID
        self.__id=id
        self.__name=name
        self.__name = name
        

class Plant_Zone(object):
    def __init__(self, PlantID,ZoneID, Prov, City, County, create_time,modified_time):
        self.__PlantID = PlantID
        self.__ZoneID = ZoneID
        self.__Prov = Prov
        self.__City = City
        self.__County = County
        self.__create_time = create_time
        self.__modified_time=modified_time
