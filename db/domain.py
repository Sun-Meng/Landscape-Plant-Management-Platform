class CareJob(object):
    def __init__(self, JobID,WorkerID,PlantID,Name, Date, Location,RegularJob,Result,create_time,modified_time):
        self.JobID = JobID
        self.WorkerID = WorkerID
        self.PlantID=PlantID
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
        
class User(object):
     def __init__(self,id,psw,type):
        self.id=id
        self.psw=psw
        self.type=type
        
class Monitor(object):
    def __init__(self, resultID, HealthStatus, name, create_time, update_time, PlantID, equipmentID):
        self.resultID = resultID
        self.HealthStatus = HealthStatus
        self.name = name
        self.create_time = create_time
        self.update_time = update_time
        self.PlantID = PlantID
        self.equipmentID = equipmentID
        
    def get_resultID(self):
        return self.resultID
    
    def get_HealthStatus(self):
        return self.HealthStatus
    
    def get_name(self):
        return self.name
    
    def get_create_time(self):
        return self.create_time
    
    def get_update_time(self):
        return self.update_time
    
    def get_PlantID(self):
        return self.PlantID
    
    def get_equipmentID(self):
        return self.equipmentID

class Monitoring_Equipment(object):
    def __init__(self, equipmentID, time, place, object,personID):
        self.equipmentID = equipmentID
        self.time = time
        self.place = place
        self.object = object
        self.personID=personID
        
    def get_equipmentID(self):
        return self.equipmentID
    
    def get_time(self):
        return self.time
    
    def get_place(self):
        return self.place
    
    def get_object(self):
        return self.object
        
class Monitoring_Personnel(object):
    def __init__(self, personID, name, sex, birth, tel, create_time, update_time):
        self.personID = str(personID)
        self.name = str(name)
        self.sex = str(sex)
        self.birth = str(birth)
        self.tel = str(tel)
        self.create_time = str(create_time)
        self.update_time = str(update_time)

    
    def get_personID(self):
        return self.personID
    
    def get_name(self):
        return self.name
    
    def get_sex(self):
        return self.sex
    
    def get_create_time(self):
        return self.create_time
    
    def get_update_time(self):
        return self.update_time
    
    def get_birth(self):
        return self.birth
    
    def get_tel(self):
        return self.tel

class Illustration:
    def __init__(self, IllustrationID, IllustrationDescription, IllustrationName):
        self.IllustrationID = IllustrationID
        self.IllustrationDescription = IllustrationDescription
        self.IllustrationName = IllustrationName

    def output(self):
        print(vars(self))

class Usage:
    def __init__(self, UsageID, Dosage, PestID, MedicineID):
        self.UsageID = UsageID
        self.Dosage = Dosage
        self.PestID = PestID
        self.MedicineID = MedicineID
    def output(self):
        print(vars(self))   

class Medicines:
    def __init__(self, MedicineID, MedicineName, ExpirationPeriod):
        self.MedicineID = MedicineID
        self.MedicineName = MedicineName
        self.ExpirationPeriod = ExpirationPeriod
    def output(self):
        print(vars(self))

class Prevent:
    def __init__(self, MeasureID, PlantID, PestID):
        self.MeasureID = MeasureID
        self.PlantID = PlantID
        self.PestID = PestID
    def output(self):
        print(vars(self))

class PestInfo:
    def __init__(self, PestID, PestName, PreventionMethod):
        self.PestID = PestID
        self.PestName = PestName
        self.PreventionMethod = PreventionMethod
    def output(self):
        print(vars(self))

class Plants:
    def __init__(self, PlantID, Name,Alias, MorphologicalFeatures, CultivationKeyPoints, ApplicationValue, PlantIntroduction, Creator, FamilyID,GenusID,SpeciesID,ZoneID,CreationTime, UpdateTime):
        self.PlantID = PlantID
        self.Name=Name
        self.Alias = Alias
        self.MorphologicalFeatures = MorphologicalFeatures
        self.CultivationKeyPoints = CultivationKeyPoints
        self.ApplicationValue = ApplicationValue
        self.PlantIntroduction = PlantIntroduction
        self.Creator = Creator
        self.FamilyID=FamilyID
        self.GenusID=GenusID
        self.SpeciesID=SpeciesID
        self.ZoneID=ZoneID
        self.CreationTime = CreationTime
        self.UpdateTime = UpdateTime
    def output(self):
        print(vars(self))
        
class Shooting:
    def __init__(self, ShootingID, ShootingLocation, Photographer, PlantID, IllustrationID):
        self.ShootingID = ShootingID
        self.ShootingLocation = ShootingLocation
        self.Photographer = Photographer
        self.PlantID = PlantID
        self.IllustrationID = IllustrationID
    def output(self):
        print(vars(self))
