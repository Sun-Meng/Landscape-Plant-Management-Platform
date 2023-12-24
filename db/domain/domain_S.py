class CareJob(object):
    def __init__(self, JobID,WorkerID,Name, Date, Location,RegularJob,Result,create_time,modified_time):
        self.JobID = JobID
        self.WorkerID = WorkerID
        self.Name = Name
        self.Date = Date
        self.Location = Location
        self.RegularJob=RegularJob
        self.Result=Result
        self.create_time = create_time
        self.modified_time=modified_time


class CareWorker(object):
    def __init__(self, ID, Name, Sex, Birth, Tel,create_time,modified_time):
        self.ID = ID
        self.Name = Name
        self.Sex = Sex
        self.Birth = Birth
        self.Tel = Tel
        self.create_time = create_time
        self.modified_time=modified_time

    

class PlantFamily(object):
     def __init__(self, id,name,info):
        self.id=id
        self.name=name
        self.info = info


class PlantGenus(object):
     def __init__(self, id,name,info):
        self.id=id
        self.name=name
        self.info = info


class PlantSpecies(object):
    def __init__(self,id,name,info):
        self.id=id
        self.name=name
        self.info = info
        

class PlantZone(object):
    def __init__(self,ZoneID, Prov, City, County, create_time,modified_time):
        self.ZoneID = ZoneID
        self.Prov = Prov
        self.City = City
        self.County = County
        self.create_time = create_time
        self.modified_time=modified_time
