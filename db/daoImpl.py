import sys
from datetime import datetime
sys.path.append("../..")
import pandas as pd
from db.domain import *
from db.dao import *
from db.utils.BaseDao import *


class careJob_dao_Impl(base_dao,careJob_dao):
    
    def __init__(self):
        self.connection = self.get_conn()

    def insert(self,CareJob) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("INSERT INTO CareJob VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (CareJob.JobID, CareJob.WorkerID, CareJob.PlantID,CareJob.Name,CareJob.Date,CareJob.Location,CareJob.RegularJob,CareJob.Result,CareJob.create_time,CareJob.modified_time))
        #self.connection.commit()
        cursor.close()

    def delete(self,CareJobID):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("DELETE FROM CareJob WHERE CareJobID=%s", (CareJobID))
        #self.connection.commit()
        cursor.close()
    
    def update(self,CareJob):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("UPDATE CareJob SET WorkerID=%s, PlantID=%s,Name=%s,Date=%s,Location=%s,RegularJob=%s,Result=%s,modified_time=%s WHERE JobID=%s",
                                (CareJob.WorkerID,CareJob.PlantID, CareJob.Name,CareJob.Date,CareJob.Location,CareJob.RegularJob,CareJob.Result,CareJob.modified_time,CareJob.JobID))
        # self.conn.commit()
        cursor.close()

    def update_JobStatus(self,id,status)->bool:
        try:
            cursor = self.connection.cursor()
            #插入sql
            cursor.execute("UPDATE CareJob SET Result=%s WHERE workerID=%s",
                                    (status,id))
            # self.conn.commit()
            cursor.close()
            return True
        except:
            return False
        

    def select(self,sql):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute(sql)
        results = cursor.fetchall()
        print(pd.DataFrame(list(results)).shape)    #用于验证是否成功读入数据库内容
        # self.connection.commit()
        cursor.close()
        return results
    
    def select_workerName(self,id):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute(
            '''
                select worker_name 
                from CareWorker as wk inner join CareJob as job on job.workerID=wk.workerID
                where job.workerID=%s 
            ''',(id))
        result = cursor.fetchone()

        # self.connection.commit()
        cursor.close()
        return result[0]
    
    def select_by_id(self,id):
        cursor = self.connection.cursor()
        cursor.execute(
            '''
                SELECT JobID,JobTitle,date,location,p.Name,HealthStatus,RegularJob,result 
                FROM CareWorker as wk 
                    inner join CareJob as job on job.workerID=wk.workerID 
                    inner join Plants as p on p.PlantID=job.PlantID 
                    inner join Monitor as m on m.PlantID=p.PlantID
					inner join Prevent as pvn on pvn.PlantID=p.PlantID
					inner join PestInfo as pest on pest.PestID=pvn.PestDiseaseID 
                WHERE job.workerID=%s
             ''',(id,))
        results = cursor.fetchall()
        print(pd.DataFrame(list(results)).shape)    #用于验证是否成功读入数据库内容
        cursor.close()
        return results
    


class careWorker_dao_Impl(base_dao,careWorker_dao):
    
    def __init__(self):
        self.connection = self.get_conn()

    def insert(self,CareWorker):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("INSERT INTO CareWorker VALUES (%s, %s, %s,%s,%s,%s,%s)",
                                (CareWorker.ID,CareWorker.Name,CareWorker.Sex,CareWorker.Birth,CareWorker.Tel,CareWorker.create_time,CareWorker.modified_time))
        #self.connection.commit()
        cursor.close()
    
    def update(self,CareWorker) :
        cursor = self.connection.cursor()
        cursor.execute("UPDATE CareWorker SET Name=%s,Sex=%s,Birth=%s,Tel=%s,modified_time=%s WHERE WorkerID=%s",
                                (CareWorker.Name,CareWorker.Sex,CareWorker.Birth,CareWorker.Tel,CareWorker.modified_time,CareWorker.ID))
        #self.connection.commit()
        cursor.close()
   
    def delete(self,CareWorkerID):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("DELETE FROM CareWorker WHERE CareWorkerID=%s", (CareWorkerID))
        #self.connection.commit()
        cursor.close()
    
    def select(self,sql) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute(sql)
        #self.connection.commit()
        cursor.close()

    def select_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM CareWorker")
        results = cursor.fetchall()
        print(pd.DataFrame(list(results)).shape)
        cursor.close()
        return results
   

class plant_Family_dao_Impl(base_dao,plant_Family_dao):

    def __init__(self):
        self.connection = self.get_conn()

    def insert(self,PlantFamily):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Plant_Family VALUES (%s, %s,%s)",
                                (PlantFamily.id, PlantFamily.name,PlantFamily.info))
        #self.connection.commit()
        cursor.close()
    
    def update(self,PlantFamily)->bool:
        try:
            cursor = self.connection.cursor()
            #插入sql
            cursor.execute("UPDATE Plant_Family SET  name=%s,info=%s WHERE id=%s"  ,
                                    (PlantFamily.name,PlantFamily.info,PlantFamily.id))
            #self.connection.commit()
            cursor.close()
            return True
        except:
            return False
    
    def delete(self,PlantFamilyID):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("DELETE FROM Plant_Family WHERE id=%s", (PlantFamilyID))
        #self.connection.commit()
        cursor.close()
  
    def select(self,sql) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute(sql)
        #self.connection.commit()
        cursor.close()

class plant_Genus_dao_Impl(base_dao,plant_Genus_dao):

    def __init__(self):
        self.connection = self.get_conn()
   
    def insert(self,PlantGenus):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Plant_Genus VALUES (%s, %s,%s)",
                                (PlantGenus.id, PlantGenus.name,PlantGenus.info))
        #self.connection.commit()
        cursor.close()
    
    def update(self,PlantGenus)->bool:
        try:
            cursor = self.connection.cursor()
            #插入sql
            cursor.execute("UPDATE Plant_Genus SET name=%s,info=%s WHERE id=%s",
                                    (PlantGenus.name,PlantGenus.info, PlantGenus.id))

            #self.connection.commit()
            cursor.close()
            return True
        except:
            return False
    
    def delete(self,PlantGenusID):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("DELETE FROM Plant_Genus WHERE id=%s", (PlantGenusID))

        #self.connection.commit()
        cursor.close()
  
    def select(self,sql) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute(sql)
        #self.connection.commit()
        cursor.close()

class plant_Species_dao_Impl(base_dao,plant_Species_dao):

    def __init__(self):
        self.connection = self.get_conn()

    def insert(self,PlantSpecies):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Plant_Species VALUES (%s, %s,%s)",
                                (PlantSpecies.id, PlantSpecies.name,PlantSpecies.info))
        #self.connection.commit()
        cursor.close()
    
    def update(self,PlantSpecies)->bool :
        try:
            cursor = self.connection.cursor()
            #插入sql
            cursor.execute("UPDATE Plant_Species SET name=%s,info=%s, id=%s",
                                    (PlantSpecies.name,PlantSpecies.info,PlantSpecies.id))
            #self.connection.commit()
            cursor.close()
            return True
        except:
            return False
    def delete(self,PlantSpeciesID):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("DELETE FROM Plant_Species WHERE id=%s", (PlantSpeciesID))

        #self.connection.commit()
        cursor.close()
  
    def select(self,sql) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute(sql)
        #self.connection.commit()
        cursor.close()

class plant_Zone_dao_Impl(base_dao,plant_Zone_dao):

    def __init__(self):
        self.connection = self.get_conn()

    def insert(self,PlantZone):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Plant_Zone VALUES ( %s, %s,%s,%s,%s,%s)",
                                ( PlantZone.ZoneID, PlantZone.Prov,PlantZone.City,PlantZone.County,PlantZone.create_time,PlantZone.modified_time))
        #self.connection.commit()
        cursor.close()
    
    def update(self,PlantZone)->bool:
        try:
            cursor = self.connection.cursor()
            #插入sql
            cursor.execute("UPDATE Plant_Zone SET  prov=%s,city=%s,county=%s,modified_time=%s WHERE ZoneID=%s",
                                    (PlantZone.Prov,PlantZone.City,PlantZone.County,PlantZone.modified_time,PlantZone.ZoneID))
            #self.connection.commit()
            cursor.close()
            return True
        except:
            return False     
    
    def delete(self,PlantZoneID):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("DELETE FROM Plant_Zone WHERE id=%s", (PlantZoneID))

        #self.connection.commit()
        cursor.close()
  
    def select(self,sql) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute(sql)
        #self.connection.commit()
        cursor.close()

class user_dao_Impl(base_dao,user_dao):

    def __init__(self):
        self.connection = self.get_conn()

    def insert(self,User):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO [User] VALUES (%s,%s,%s)",(User.id,User.psw,User.type))
        #self.connection.commit()
        cursor.close()
    
    def update(self,User) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("UPDATE [User] SET psw=%s,type=%s WHERE id=%s",(User.psw,User.type,User.id))
        #self.connection.commit()
        cursor.close()
    
    def delete(self,userID):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("DELETE FROM [User] WHERE id=%s", (userID))
        #self.connection.commit()
        cursor.close()
  
    def select(self,sql) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute(sql)
        #self.connection.commit()
        cursor.close()

    def login(self, userId, password):
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM [User] WHERE id = %s AND psw = %s", (userId, password))
        count = cursor.fetchone()[0]
        if count == 1:
            return True
        else:
            return False

    def type(self, userId=None, password=None):
        if userId is None or password is None:
            return None

        cursor = self.connection.cursor()
        cursor.execute("SELECT type FROM [User] WHERE id = %s AND psw = %s", (userId, password))

        result = cursor.fetchone()
        if result is not None:
            return result[0]
        else:
            return None


class Monitor_dao_Impl(base_dao,Monitor_dao):
    
    def __init__(self):
        self.connection = self.get_conn()

    def insert(self,Monitor) :
        cursor = self.connection.cursor()
        cursor.execute("insert into Monitor values(%s,%s,%s,%s,%s,%s,%s)",(Monitor.resultID,Monitor.PlantID,Monitor.equipmentID,Monitor.HealthStatus,Monitor.name,Monitor.create_time,Monitor.update_time))
        self.connection.commit()
        cursor.close()

    def delete(self,Monitor):
        cursor = self.connection.cursor()
        cursor.execute("delete from Monitor where resultID=%s",(Monitor.resultID))
        self.connection.commit()
        cursor.close()
    
    def update(self,Monitor):
        cursor = self.connection.cursor()
        cursor.execute("update Monitor set HealthStatus = %s, name = %s, create_time = %s, update_time = %s, PlantID = %s, equipmentID = %s where resultID = %s",(Monitor.HealthStatus, Monitor.name, Monitor.create_time, Monitor.update_time, Monitor.PlantID, Monitor.equipmentID, Monitor.resultID))
        self.connection.commit()
        cursor.close()

    def select(self,resultID):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Monitor WHERE resultID=%s", (resultID))
        result = cursor.fetchall()
        cursor.close()
        return result


class Monitoring_Equipment_dao_Impl(base_dao,Monitoring_Equipment_dao):
    
    def __init__(self):
        self.connection = self.get_conn()

    def insert(self,Monitoring_Equipment) :
        cursor = self.connection.cursor()
        cursor.execute("insert into Monitoring_Equipment values(%s,%s,%s,%s,%s)",(Monitoring_Equipment.equipmentID,Monitoring_Equipment.time,Monitoring_Equipment.place,Monitoring_Equipment.object,Monitoring_Equipment.personID))
        self.connection.commit()
        cursor.close()

    def delete(self,Monitoring_Equipment):
        cursor = self.connection.cursor()
        cursor.execute("delete from Monitoring_Equipment where equipmentID=%s",(Monitoring_Equipment.equipmentID))
        self.connection.commit()
        cursor.close()
    
    def update(self,Monitoring_Equipment):
        cursor = self.connection.cursor()
        cursor.execute("update Monitoring_Equipment set time = %s, place = %s, object = %s where equipmentID = %s",(Monitoring_Equipment.equipmentID,Monitoring_Equipment.time,Monitoring_Equipment.place,Monitoring_Equipment.object))
        self.connection.commit()
        cursor.close()

    def select(self,equipmentID):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Monitoring_Equipment WHERE equipmentID=%s", (equipmentID))
        result = cursor.fetchall()
        cursor.close()
        return result


class Monitoring_Personnel_dao_Impl(base_dao,Monitoring_Personnel_dao):
    
    def __init__(self):
        self.connection = self.get_conn()

    def insert(self,Monitoring_Personnel) :
        cursor = self.connection.cursor()
        cursor.execute("insert into Monitoring_Personnel values(%s,%s,%s,%s,%s,%s,%s)",(Monitoring_Personnel.personID,Monitoring_Personnel.name,Monitoring_Personnel.sex,Monitoring_Personnel.birth,Monitoring_Personnel.tel,Monitoring_Personnel.create_time,Monitoring_Personnel.update_time))
        self.connection.commit()
        cursor.close()

    def delete(self,Monitoring_Personnel):
        cursor = self.connection.cursor()
        cursor.execute("delete from Monitoring_Personnel where personID=%s",(Monitoring_Personnel.personID))
        self.connection.commit()
        cursor.close()
    
    def update(self,Monitoring_Personnel):
        cursor = self.connection.cursor()
        cursor.execute("update Monitoring_Personnel set name = %s, sex = %s, create_time = %s, update_time = %s, birth = %s, tel = %s where personID = %s",(Monitoring_Personnel.personID,Monitoring_Personnel.name,Monitoring_Personnel.sex,Monitoring_Personnel.create_time,Monitoring_Personnel.update_time,Monitoring_Personnel.birth,Monitoring_Personnel.tel))
        self.connection.commit()
        cursor.close()

    def select(self,PersonID):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Monitoring_Personnel WHERE PersonID=%s", (PersonID))
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def select_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Monitoring_Personnel")
        results = cursor.fetchall()
        print(pd.DataFrame(list(results)).shape)
        cursor.close()
        return results
    

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
            cursor.execute("DELETE FROM Illustration WHERE IllustrationID=%s", (IllustrationID))
            # self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, Illustration) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE Illustration SET IllustrationDescription=%s, IllustrationName=%s WHERE IllustrationID=%s",
                                (Illustration.IllustrationDescription, Illustration.IllustrationName,Illustration.IllustrationID))
            # self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, IllustrationID):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Illustration WHERE IllustrationID=%s", (IllustrationID))
        result = cursor.fetchone()
        if result:
            return Illustration(result[0], result[1], result[2])
        else:
            return None

class UsageDaoImpl(base_dao,UsageDao):
    def __init__(self):
        self.connection = self.get_conn() 
        self.cursor = self.connection.cursor()
    def insert(self, Usage:Usage) -> bool:
        try:
            self.cursor.execute ("INSERT INTO Usage VALUES (%s, %s, %s, %s)",
                                (Usage.UsageID, Usage.Dosage, Usage.PestID,Usage.MedicineID))
            # self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
        
    def delete(self,UsageID) -> bool:
        try:
            self.cursor.execute("DELETE FROM Usage WHERE UsageID=%s", (UsageID))
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, Usage:Usage) -> bool:
        try:
            self.cursor.execute("UPDATE Usage SET Dosage=%s,PestID=%s, MedicineID=%s WHERE UsageID=%s",
                                (Usage.Dosage, Usage.PestID,Usage.MedicineID,Usage.UsageID))
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, UsageID):
        self.cursor.execute("SELECT * FROM Usage WHERE UsageID=%s", (UsageID))
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
            self.cursor.execute("DELETE FROM Medicines WHERE MedicineID=%s", (MedicineID))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, medicine: Medicines) -> bool:
        try:
            self.cursor.execute("UPDATE Medicines SET MedicineName=%s, ExpirationPeriod=%s WHERE MedicineID=%s ",
                                (medicine.MedicineName, medicine.ExpirationPeriod,medicine.MedicineID))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, MedicineID):
        self.cursor.execute("SELECT * FROM Medicines WHERE MedicineID=%s", (MedicineID))
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
            self.cursor.execute("DELETE FROM Prevent WHERE MeasureID=%s", (MeasureID))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, prevent: Prevent) -> bool:
        try:
            self.cursor.execute("UPDATE Prevent SET PlantID=%s, PestID=%s WHERE MeasureID=%s",
                                (prevent.PlantID, prevent.PestID,prevent.MeasureID))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, MeasureID):
        self.cursor.execute("SELECT * FROM Prevent WHERE MeasureID=%s", (MeasureID))
        result = self.cursor.fetchone()
        if result:
            return Prevent(result[0], result[1], result[2])
        else:
            return None
        
    def select_by_id(self,id,plantStatus):
        self.cursor.execute(
            '''
                SELECT p.PlantID,p.Name,PestName,MedicineName,Dosage,ExpirationPeriod,PreventionMethod
                FROM CareWorker as wk 
                    inner join CareJob as job on job.workerID=wk.workerID 
                    inner join Plants as p on p.PlantID=job.PlantID 
                    inner join Monitor as m on m.PlantID=p.PlantID
                    inner join Prevent as pvn on pvn.PlantID=p.PlantID
                    inner join PestInfo as pest on pest.PestID=pvn.PestDiseaseID
                    inner join Usage as u on u.PestID=pest.PestID
                    inner join Medicines as mdc on mdc.MedicineID=u.MedicineID
                WHERE job.workerID=%s AND HealthStatus like %s
                ''',(id,plantStatus,))
        results = self.cursor.fetchall()
        print(pd.DataFrame(list(results)).shape)    #用于验证是否成功读入数据库内容
        # try:
        #     self.cursor.close()
        # except InterfaceError as e:
        #     end=e
        return results

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
            self.cursor.execute("DELETE FROM PestInfo WHERE PestID=%s", (PestID))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, pest_info: PestInfo) -> bool:
        try:
            self.cursor.execute("UPDATE PestInfo SET PestName=%s, PreventionMethod=%s WHERE PestID=%s",
                                (pest_info.PestName, pest_info.PreventionMethod, pest_info.PestID))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, PestID):
        self.cursor.execute("SELECT * FROM PestInfo WHERE PestID=%s", (PestID))
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
            self.cursor.execute("INSERT INTO Plants VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                (plant.PlantID,plant.Name,plant.Alias, plant.MorphologicalFeatures, plant.CultivationKeyPoints, plant.ApplicationValue, plant.PlantIntroduction, plant.Creator, plant.FamilyID, plant.GenusID,plant.SpeciesID,plant.ZoneID,plant.CreationTime,plant.UpdateTime))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, PlantID) -> bool:
        try:
            self.cursor.execute("DELETE FROM Plants WHERE PlantID=%s", (PlantID))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, plant: Plants) -> bool:
        try:
            self.cursor.execute("UPDATE Plants SET Name=%s, Alias=%s, MorphologicalFeatures=%s, CultivationKeyPoints=%s, ApplicationValue=%s, PlantIntroduction=%s, Creator=%s,FamilyID=%s,GenusID=%s,SpeciesID=%s,ZoneID=%s,CreationTime=%s, UpdateTime=%s WHERE PlantID=%s",
                                (plant.Name,plant.Alias, plant.MorphologicalFeatures, plant.CultivationKeyPoints, plant.ApplicationValue, plant.PlantIntroduction, plant.Creator,plant.FamilyID,plant.GenusID,plant.SpeciesID,plant.ZoneID,plant.CreationTime,plant.UpdateTime,plant.PlantID ))
            # self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, PlantID):
        self.cursor.execute("SELECT * FROM Plants WHERE PlantID=%s", (PlantID))
        result = self.cursor.fetchone()
        if result:
            return Plants(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8],result[9],result[10],result[11],result[12],result[13])
        else:
            return None
        
    def selectAll(self):
        self.cursor.execute("SELECT * FROM Plants")
        results = self.cursor.fetchone()
        return results

        
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
            self.cursor.execute("DELETE FROM Shooting WHERE ShootingID=%s", (ShootingID))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, shooting: Shooting) -> bool:
        try:
            self.cursor.execute("UPDATE Shooting SET ShootingLocation=%s, Photographer=%s, PlantID=%s, IllustrationID=%s WHERE ShootingID=%s",
                                (shooting.ShootingLocation, shooting.Photographer, shooting.PlantID, shooting.IllustrationID,shooting.ShootingID))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, ShootingID):
        self.cursor.execute("SELECT * FROM Shooting WHERE ShootingID=%s", (ShootingID))
        result = self.cursor.fetchone()
        if result:
            return Shooting(result[0], result[1], result[2], result[3], result[4])
        else:
            return None