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
