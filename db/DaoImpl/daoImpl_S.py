import sys
sys.path.append("../..")

import pandas as pd

from db.domain.domain_S import *

from db.Dao.dao_S import careJob_dao, careWorker_dao, plant_Family_dao, plant_Genus_dao, plant_Species_dao, plant_Zone_dao

from db.utils.dao import *

class careJob_dao_Impl(base_dao,careJob_dao):
    
    def __init__(self):
        self.connection = self.get_conn()

    def insert(self,CareJob) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("INSERT INTO CareJob VALUES (?, ?, ?,?,?,?,?)",
                                (CareJob.JobID, CareJob.WorkerID, CareJob.Name,CareJob.Date,CareJob.Location,CareJob.RegularJob,CareJob.Result))
        #self.connection.commit()
        cursor.close()

    def delete(self,CareJobID):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("DELETE FROM CareJob WHERE CareJobID=?", (CareJobID,))
        #self.connection.commit()
        cursor.close()
    
    def update(self,CareJob):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("UPDATE CareJob SET JobID=?, WorkerID=?, Name=?,Date=?,Location=?,RegularJob=?,Result=?",
                                (CareJob.JobID, CareJob.WorkerID, CareJob.Name,CareJob.Date,CareJob.Location,CareJob.RegularJob,CareJob.Result))
        # self.conn.commit()
        cursor.close()

    def select(self,sql):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute(sql)
        results = cursor.fetchall()
        print(pd.DataFrame(list(results)).shape)    #用于验证是否成功读入数据库内容
        # self.connection.commit()
        cursor.close()
        return results
    
    def select_by_id(self,id):
        cursor = self.connection.cursor()
        cursor.execute(("SELECT JobID,JobTitle,date,location,worker_name,Alias,result FROM CareWorker as wk inner join CareJob as job on job.workerID=wk.workerID innerjoin Plants as p on p.PlantID=job.PlantID WHERE =?", (id,)))
        results = cursor.fetchall()
        print(pd.DataFrame(list(results)).shape)    #用于验证是否成功读入数据库内容
        cursor.close()
        return results
    
#   只返回 养护结果
    # def select_caring_result(self):
    #     cursor = self.connection.cursor()
    #     sql='''
    #         SELECT JobID,JobTitle,worker_name,result 
    #         FROM CareJob as job inner join Gardener as gd on job.workerID=gd.workerID
    #     '''
    #     cursor.execute(sql)
    #     results = cursor.fetchall()
    #     return results

    # def select_all(self):
    #     cursor = self.connection.cursor()
    #     cursor.execute("SELECT * FROM CareJob")
    #     results = cursor.fetchall()
    #     print(pd.DataFrame(list(results)).shape)#用于验证是否成功读入数据库内容

    #     return results

class careWorker_dao_Impl(base_dao,careWorker_dao):
    
    def _init__(self):
        self.connection = self.get_conn()

    def insert(self,CareWorker):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("INSERT INTO CareWorker VALUES (?, ?, ?,?,?)",
                                (CareWorker.WorkerID,CareWorker.Name,CareWorker.Sex,CareWorker.Birth,CareWorker.Tel))
        #self.connection.commit()
        cursor.close()
    
    def update(self,CareWorker) :
        cursor = self.connection.cursor()
        cursor.execute("UPDATE CareWorker SET WorkerID=?, Name=?,Sex=?,Birth=?,Tel=?",
                                (CareJob.WorkerID, CareJob.Name,CareJob.Sex,CareJob.Birth,CareJob.Tel))
        #self.connection.commit()
        cursor.close()
   
    def delete(self,CareWorkerID):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("DELETE FROM CareWorker WHERE CareWorkerID=?", (CareWorkerID,))
        #self.connection.commit()
        cursor.close()
    
    def select(self,sql) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute(sql)
        #self.connection.commit()
        cursor.close()


   

class plant_Family_dao_Impl(base_dao,plant_Family_dao):
    
    def insert(self,PlantFamily):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Plant_Family VALUES (?, ?, ?,?)",
                                (PlantFamily.PlantID, PlantFamily.id, PlantFamily.name,PlantFamily.info))
        #self.connection.commit()
        cursor.close()
    
    def update(self,PlantFamily) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("UPDATE Plant_Family SET PlantID=?, id=?, name=?,info=?",
                                (PlantFamily.PlantID, PlantFamily.id, PlantFamily.name,PlantFamily.info))
        #self.connection.commit()
        cursor.close()
    
    def delete(self,PlantFamilyID):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("DELETE FROM Plant_Family WHERE PlantID=?", (PlantFamilyID,))
        #self.connection.commit()
        cursor.close()
  
    def select(self,sql) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute(sql)
        #self.connection.commit()
        cursor.close()

class plant_Genus_dao_Impl(base_dao,plant_Genus_dao):
   
    def insert(self,PlantGenus):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Plant_Genus VALUES (?, ?, ?,?)",
                                (PlantGenus.PlantID, PlantGenus.id, PlantGenus.name,PlantGenus.info))
        #self.connection.commit()
        cursor.close()
    
    def update(self,PlantGenus) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("UPDATE Plant_Genus SET PlantID=?, id=?, name=?,info=?",
                                (PlantGenus.PlantID, PlantGenus.id, PlantGenus.name,PlantGenus.info))

        #self.connection.commit()
        cursor.close()
    
    def delete(self,PlantGenusID):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("DELETE FROM Plant_Genus WHERE PlantID=?", (PlantGenusID,))

        #self.connection.commit()
        cursor.close()
  
    def select(self,sql) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute(sql)
        #self.connection.commit()
        cursor.close()

class plant_Species_dao_Impl(base_dao,plant_Species_dao):

    def insert(self,PlantSpecies):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Plant_Species VALUES (?, ?, ?,?)",
                                (PlantSpecies.PlantID, PlantSpecies.id, PlantSpecies.name,PlantSpecies.info))
        #self.connection.commit()
        cursor.close()
    
    def update(self,PlantSpecies) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("UPDATE Plant_Species SET PlantID=?, id=?, name=?,info=?",
                                (PlantSpecies.PlantID, PlantSpecies.id, PlantSpecies.name,PlantSpecies.info))

        #self.connection.commit()
        cursor.close()
    
    def delete(self,PlantSpeciesID):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("DELETE FROM Plant_Species WHERE PlantID=?", (PlantSpeciesID,))

        #self.connection.commit()
        cursor.close()
  
    def select(self,sql) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute(sql)
        #self.connection.commit()
        cursor.close()

class plant_Zone_dao_Impl(base_dao,plant_Zone_dao):
    def insert(self,PlantZone):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Plant_Zone VALUES (?, ?, ?,?)",
                                (PlantZone.PlantID, PlantZone.id, PlantZone.name,PlantZone.info))
        #self.connection.commit()
        cursor.close()
    
    def update(self,PlantZone) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("UPDATE Plant_Zone SET PlantID=?, id=?, name=?,info=?",
                                (PlantZone.PlantID, PlantZone.id, PlantZone.name,PlantZone.info))

        #self.connection.commit()
        cursor.close()
    
    def delete(self,PlantZoneID):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("DELETE FROM Plant_Zone WHERE PlantID=?", (PlantZoneID,))

        #self.connection.commit()
        cursor.close()
  
    def select(self,sql) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute(sql)
        #self.connection.commit()
        cursor.close()