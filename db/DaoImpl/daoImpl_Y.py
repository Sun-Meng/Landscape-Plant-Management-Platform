import sys
sys.path.append("..")
from Dao.dao_Y import *
from utils.Dao_base import *
from domain.domain_Y import *
from utils.Dao_base import *

class IllustrationDaoImpl(base_dao,IllustrationDao):
    def __init__(self):
        self.connection = self.get_conn() 
        cursor = self.connection.cursor()
    def insert(self, Illustration:Illustration) -> bool:
        try:
            self.cursor.execute ("INSERT INTO Illustration VALUES (?, ?, ?)",
                                (Illustration.IllustrationID, Illustration.IllustrationDescription, Illustration.IllustrationName))
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
        
    def delete(self,IllustrationID) -> bool:
        try:
            self.cursor.execute("DELETE FROM Illustration WHERE IllustrationID=?", (IllustrationID,))
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, Illustration:Illustration) -> bool:
        try:
            self.cursor.execute("UPDATE Illustration SET IllustrationID=?, IllustrationDescription=?, IllustrationName=?",
                                (Illustration.IllustrationID, Illustration.IllustrationDescription,  Illustration.IllustrationName))
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, IllustrationID):
        self.cursor.execute("SELECT * FROM Illustration WHERE IllustrationID=?", (IllustrationID,))
        result = self.cursor.fetchone()
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
            self.cursor.execute ("INSERT INTO Usage VALUES (?, ?, ?, ?)",
                                (Usage.UsageID, Usage.Dosage, Usage.PestID,Usage.MedicineID))
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
        
    def delete(self,UsageID) -> bool:
        try:
            self.cursor.execute("DELETE FROM Usage WHERE UsageID=?", (UsageID,))
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, Usage:Usage) -> bool:
        try:
            self.cursor.execute("UPDATE Usage SET UsageID=?, PestID=?, MedicineID=?",
                                (Usage.UsageID, Usage.Dosage,  Usage.PestID,Usage.MedicineID))
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, UsageID):
        self.cursor.execute("SELECT * FROM Usage WHERE UsageID=?", (UsageID,))
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
            self.cursor.execute("INSERT INTO Medicines VALUES (?, ?, ?)",
                                (medicine.MedicineID, medicine.MedicineName, medicine.ExpirationPeriod))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, MedicineID) -> bool:
        try:
            self.cursor.execute("DELETE FROM Medicines WHERE MedicineID=?", (MedicineID,))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, medicine: Medicines) -> bool:
        try:
            self.cursor.execute("UPDATE Medicines SET MedicineID=?, MedicineName=?, ExpirationPeriod=?",
                                (medicine.MedicineID, medicine.MedicineName, medicine.ExpirationPeriod))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, MedicineID):
        self.cursor.execute("SELECT * FROM Medicines WHERE MedicineID=?", (MedicineID,))
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
            self.cursor.execute("INSERT INTO Prevent VALUES (?, ?, ?)",
                                (prevent.MeasureID, prevent.PlantID, prevent.PestID))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, MeasureID) -> bool:
        try:
            self.cursor.execute("DELETE FROM Prevent WHERE MeasureID=?", (MeasureID,))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, prevent: Prevent) -> bool:
        try:
            self.cursor.execute("UPDATE Prevent SET MeasureID=?, PlantID=?, PestID=?",
                                (prevent.MeasureID, prevent.PlantID, prevent.PestID))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, MeasureID):
        self.cursor.execute("SELECT * FROM Prevent WHERE MeasureID=?", (MeasureID,))
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
            self.cursor.execute("INSERT INTO PestInfo VALUES (?, ?, ?)",
                                (pest_info.PestID, pest_info.PestName, pest_info.PreventionMethod))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, PestID) -> bool:
        try:
            self.cursor.execute("DELETE FROM PestInfo WHERE PestID=?", (PestID,))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, pest_info: PestInfo) -> bool:
        try:
            self.cursor.execute("UPDATE PestInfo SET PestID=?, PestName=?, PreventionMethod=?",
                                (pest_info.PestID, pest_info.PestName, pest_info.PreventionMethod))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, PestID):
        self.cursor.execute("SELECT * FROM PestInfo WHERE PestID=?", (PestID,))
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
            self.cursor.execute("INSERT INTO Plants VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                (plant.PlantID, plant.Alias, plant.MorphologicalFeatures, plant.CultivationKeyPoints, plant.ApplicationValue, plant.PlantIntroduction, plant.Creator, plant.CreationTime, plant.UpdateTime))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, PlantID) -> bool:
        try:
            self.cursor.execute("DELETE FROM Plants WHERE PlantID=?", (PlantID,))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, plant: Plants) -> bool:
        try:
            self.cursor.execute("UPDATE Plants SET PlantID=?, Alias=?, MorphologicalFeatures=?, CultivationKeyPoints=?, ApplicationValue=?, PlantIntroduction=?, Creator=?, CreationTime=?, UpdateTime=?",
                                (plant.PlantID, plant.Alias, plant.MorphologicalFeatures, plant.CultivationKeyPoints, plant.ApplicationValue, plant.PlantIntroduction, plant.Creator, plant.CreationTime, plant.UpdateTime))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, PlantID):
        self.cursor.execute("SELECT * FROM Plants WHERE PlantID=?", (PlantID,))
        result = self.cursor.fetchone()
        if result:
            return Plants(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8])
        else:
            return None

        
class ShootingDaoImpl(base_dao, ShootingDao):
    def __init__(self):
        self.connection = self.get_conn() 
        self.cursor = self.connection.cursor()

    def insert(self, shooting: Shooting) -> bool:
        try:
            self.cursor.execute("INSERT INTO Shooting VALUES (?, ?, ?, ?, ?)",
                                (shooting.ShootingID, shooting.ShootingLocation, shooting.Photographer, shooting.PlantID, shooting.IllustrationID))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, ShootingID) -> bool:
        try:
            self.cursor.execute("DELETE FROM Shooting WHERE ShootingID=?", (ShootingID,))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, shooting: Shooting) -> bool:
        try:
            self.cursor.execute("UPDATE Shooting SET ShootingID=?, ShootingLocation=?, Photographer=?, PlantID=?, IllustrationID=?",
                                (shooting.ShootingID, shooting.ShootingLocation, shooting.Photographer, shooting.PlantID, shooting.IllustrationID))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, ShootingID):
        self.cursor.execute("SELECT * FROM Shooting WHERE ShootingID=?", (ShootingID,))
        result = self.cursor.fetchone()
        if result:
            return Shooting(result[0], result[1], result[2], result[3], result[4])
        else:
            return None
