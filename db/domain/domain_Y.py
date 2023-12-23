class Illustration:
    def __init__(self, IllustrationID, IllustrationDescription, IllustrationName):
        self.IllustrationID = IllustrationID
        self.IllustrationDescription = IllustrationDescription
        self.IllustrationName = IllustrationName

class Usage:
    def __init__(self, UsageID, Dosage, PestID, MedicineID):
        self.UsageID = UsageID
        self.Dosage = Dosage
        self.PestID = PestID
        self.MedicineID = MedicineID

class Medicines:
    def __init__(self, MedicineID, MedicineName, ExpirationPeriod):
        self.MedicineID = MedicineID
        self.MedicineName = MedicineName
        self.ExpirationPeriod = ExpirationPeriod

class Prevent:
    def __init__(self, MeasureID, PlantID, PestID):
        self.MeasureID = MeasureID
        self.PlantID = PlantID
        self.PestID = PestID

class PestInfo:
    def __init__(self, PestID, PestName, PreventionMethod):
        self.PestID = PestID
        self.PestName = PestName
        self.PreventionMethod = PreventionMethod

class Plants:
    def __init__(self, PlantID, Alias, MorphologicalFeatures, CultivationKeyPoints, ApplicationValue, PlantIntroduction, Creator, CreationTime, UpdateTime):
        self.PlantID = PlantID
        self.Alias = Alias
        self.MorphologicalFeatures = MorphologicalFeatures
        self.CultivationKeyPoints = CultivationKeyPoints
        self.ApplicationValue = ApplicationValue
        self.PlantIntroduction = PlantIntroduction
        self.Creator = Creator
        self.CreationTime = CreationTime
        self.UpdateTime = UpdateTime
        
class Shooting:
    def __init__(self, ShootingID, ShootingLocation, Photographer, PlantID, IllustrationID):
        self.ShootingID = ShootingID
        self.ShootingLocation = ShootingLocation
        self.Photographer = Photographer
        self.PlantID = PlantID
        self.IllustrationID = IllustrationID
