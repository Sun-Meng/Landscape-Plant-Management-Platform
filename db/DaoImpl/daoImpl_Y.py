import sys
sys.path.append("../..")
from db.Dao.dao_Y import *
from db.utils.dao import *
from db.domain.domain_Y import *
class IllustrationDaoImpl(base_dao,IllustrationDao):
    def __init__(self):
        self.connection = self.get_conn() 
    
    def insert(self, Illustration:Illustration) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute ("INSERT INTO Illustration VALUES (%s, %s, %s)",
                                (Illustration.IllustrationID, Illustration.IllustrationDescription, Illustration.IllustrationName))
            # self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
        
    def delete(self,IllustrationID) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Illustration WHERE IllustrationID=%s", (IllustrationID,))
            # self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, Illustration) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE Illustration SET IllustrationID=%s, IllustrationDescription=%s, IllustrationName=%s",
                                (Illustration.IllustrationID, Illustration.IllustrationDescription,  Illustration.IllustrationName))
            # self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, IllustrationID):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Illustration WHERE IllustrationID=%s", (IllustrationID,))
        result = cursor.fetchone()
        if result:
            return Illustration(result[0], result[1], result[2])
        else:
            return None

class UsageDaoImpl(base_dao,UsageDao):
    def __init__(self):
        self.connection = self.get_conn() 
        cursor = self.connection.cursor()
    def insert(self, Usage:Usage) -> bool:
        try:
            self.cursor.execute ("INSERT INTO Usage VALUES (%s, %s, %s, %s)",
                                (Usage.UsageID, Usage.Dosage, Usage.PestID,Usage.MedicineID))
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
        
    def delete(self,UsageID) -> bool:
        try:
            self.cursor.execute("DELETE FROM Usage WHERE UsageID=%s", (UsageID,))
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, Usage:Usage) -> bool:
        try:
            self.cursor.execute("UPDATE Usage SET UsageID=%s, PestID=%s, MedicineID=%s",
                                (Usage.UsageID, Usage.Dosage,  Usage.PestID,Usage.MedicineID))
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, UsageID):
        self.cursor.execute("SELECT * FROM Usage WHERE UsageID=%s", (UsageID,))
        result = self.cursor.fetchone()
        if result:
            return Usage(result[0], result[1], result[2], result[3])
        else:
            return None

class MedicinesDaoImpl(base_dao, MedicinesDao):
    def __init__(self):
        self.connection = self.get_conn() 
        self.cursor = self.connection.cursor()

    def insert(self, medicine: Medicines) -> bool:
        try:
            self.cursor.execute("INSERT INTO Medicines VALUES (%s, %s, %s)",
                                (medicine.MedicineID, medicine.MedicineName, medicine.ExpirationPeriod))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, MedicineID) -> bool:
        try:
            self.cursor.execute("DELETE FROM Medicines WHERE MedicineID=%s", (MedicineID,))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, medicine: Medicines) -> bool:
        try:
            self.cursor.execute("UPDATE Medicines SET MedicineID=%s, MedicineName=%s, ExpirationPeriod=%s",
                                (medicine.MedicineID, medicine.MedicineName, medicine.ExpirationPeriod))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, MedicineID):
        self.cursor.execute("SELECT * FROM Medicines WHERE MedicineID=%s", (MedicineID,))
        result = self.cursor.fetchone()
        if result:
            return Medicines(result[0], result[1], result[2])
        else:
            return None


class PreventDaoImpl(base_dao, PreventDao):
    def __init__(self):
        self.connection = self.get_conn() 
        self.cursor = self.connection.cursor()

    def insert(self, prevent: Prevent) -> bool:
        try:
            self.cursor.execute("INSERT INTO Prevent VALUES (%s, %s, %s)",
                                (prevent.MeasureID, prevent.PlantID, prevent.PestID))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, MeasureID) -> bool:
        try:
            self.cursor.execute("DELETE FROM Prevent WHERE MeasureID=%s", (MeasureID,))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, prevent: Prevent) -> bool:
        try:
            self.cursor.execute("UPDATE Prevent SET MeasureID=%s, PlantID=%s, PestID=%s",
                                (prevent.MeasureID, prevent.PlantID, prevent.PestID))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, MeasureID):
        self.cursor.execute("SELECT * FROM Prevent WHERE MeasureID=%s", (MeasureID,))
        result = self.cursor.fetchone()
        if result:
            return Prevent(result[0], result[1], result[2])
        else:
            return None


class PestInfoDaoImpl(base_dao, PestInfoDao):
    def __init__(self):
        self.connection = self.get_conn() 
        self.cursor = self.connection.cursor()

    def insert(self, pest_info: PestInfo) -> bool:
        try:
            self.cursor.execute("INSERT INTO PestInfo VALUES (%s, %s, %s)",
                                (pest_info.PestID, pest_info.PestName, pest_info.PreventionMethod))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, PestID) -> bool:
        try:
            self.cursor.execute("DELETE FROM PestInfo WHERE PestID=%s", (PestID,))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, pest_info: PestInfo) -> bool:
        try:
            self.cursor.execute("UPDATE PestInfo SET PestID=%s, PestName=%s, PreventionMethod=%s",
                                (pest_info.PestID, pest_info.PestName, pest_info.PreventionMethod))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, PestID):
        self.cursor.execute("SELECT * FROM PestInfo WHERE PestID=%s", (PestID,))
        result = self.cursor.fetchone()
        if result:
            return PestInfo(result[0], result[1], result[2])
        else:
            return None


class PlantsDaoImpl(base_dao, PlantsDao):
    def __init__(self):
        self.connection = self.get_conn() 
        self.cursor = self.connection.cursor()

    def insert(self, plant: Plants) -> bool:
        try:
            self.cursor.execute("INSERT INTO Plants VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                (plant.PlantID, plant.Alias, plant.MorphologicalFeatures, plant.CultivationKeyPoints, plant.ApplicationValue, plant.PlantIntroduction, plant.Creator, plant.CreationTime, plant.UpdateTime))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, PlantID) -> bool:
        try:
            self.cursor.execute("DELETE FROM Plants WHERE PlantID=%s", (PlantID,))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, plant: Plants) -> bool:
        try:
            self.cursor.execute("UPDATE Plants SET PlantID=%s, Alias=%s, MorphologicalFeatures=%s, CultivationKeyPoints=%s, ApplicationValue=%s, PlantIntroduction=%s, Creator=%s, CreationTime=%s, UpdateTime=%s",
                                (plant.PlantID, plant.Alias, plant.MorphologicalFeatures, plant.CultivationKeyPoints, plant.ApplicationValue, plant.PlantIntroduction, plant.Creator, plant.CreationTime, plant.UpdateTime))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, PlantID):
        self.cursor.execute("SELECT * FROM Plants WHERE PlantID=%s", (PlantID,))
        result = self.cursor.fetchone()
        if result:
            return Plants(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8])
        else:
            return None
        
    def selectAll(self):
        self.cursor.execute("SELECT * FROM Plants")
        results = self.cursor.fetchone()
        simple_informations = []
        for result in results:
            simple_informations.append(Plants(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8]))
        return simple_informations

        
class ShootingDaoImpl(base_dao, ShootingDao):
    def __init__(self):
        self.connection = self.get_conn() 
        self.cursor = self.connection.cursor()

    def insert(self, shooting: Shooting) -> bool:
        try:
            self.cursor.execute("INSERT INTO Shooting VALUES (%s, %s, %s, %s, %s)",
                                (shooting.ShootingID, shooting.ShootingLocation, shooting.Photographer, shooting.PlantID, shooting.IllustrationID))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, ShootingID) -> bool:
        try:
            self.cursor.execute("DELETE FROM Shooting WHERE ShootingID=%s", (ShootingID,))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, shooting: Shooting) -> bool:
        try:
            self.cursor.execute("UPDATE Shooting SET ShootingID=%s, ShootingLocation=%s, Photographer=%s, PlantID=%s, IllustrationID=%s",
                                (shooting.ShootingID, shooting.ShootingLocation, shooting.Photographer, shooting.PlantID, shooting.IllustrationID))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, ShootingID):
        self.cursor.execute("SELECT * FROM Shooting WHERE ShootingID=%s", (ShootingID,))
        result = self.cursor.fetchone()
        if result:
            return Shooting(result[0], result[1], result[2], result[3], result[4])
        else:
            return None
