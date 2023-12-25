import sys
from datetime import datetime
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
        cursor.execute("INSERT INTO CareJob VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s)",
                                (CareJob.JobID, CareJob.WorkerID, CareJob.Name,CareJob.Date,CareJob.Location,CareJob.RegularJob,CareJob.Result,CareJob.create_time,CareJob.modified_time))
        #self.connection.commit()
        cursor.close()

    def delete(self,CareJobID):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("DELETE FROM CareJob WHERE CareJobID=%s", (CareJobID,))
        #self.connection.commit()
        cursor.close()
    
    def update(self,CareJob):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("UPDATE CareJob SET JobID=%s, WorkerID=%s, Name=%s,Date=%s,Location=%s,RegularJob=%s,Result=%s,modified_time=%s",
                                (CareJob.JobID, CareJob.WorkerID, CareJob.Name,CareJob.Date,CareJob.Location,CareJob.RegularJob,CareJob.Result,CareJob.modified_time))
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
    
    def select_workerName(self,id):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute(
            '''
                select worker_name 
                from CareWorker as wk inner join CareJob as job on job.workerID=wk.workerID 
            ''')
        workerName = cursor.fetchone()

        # self.connection.commit()
        cursor.close()
        return workerName
    
    def select_by_id(self,id):
        cursor = self.connection.cursor()
        cursor.execute(
            ('''
                SELECT JobID,JobTitle,date,location,Name,PestName,HealthStatus,RegularJob,result 
                FROM CareWorker as wk 
                    inner join CareJob as job on job.workerID=wk.workerID 
                    inner join Plants as p on p.PlantID=job.PlantID 
                    inner join Monitor as m on m.PlantID=p.PlantID 
                WHERE job.workerID=%s
             ''',(id,)))
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
        cursor.execute("UPDATE CareWorker SET WorkerID=%s, Name=%s,Sex=%s,Birth=%s,Tel=%s,modified_time=%s",
                                (CareWorker.ID, CareWorker.Name,CareWorker.Sex,CareWorker.Birth,CareWorker.Tel,CareWorker.modified_time))
        #self.connection.commit()
        cursor.close()
   
    def delete(self,CareWorkerID):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("DELETE FROM CareWorker WHERE CareWorkerID=%s", (CareWorkerID,))
        #self.connection.commit()
        cursor.close()
    
    def select(self,sql) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute(sql)
        #self.connection.commit()
        cursor.close()


   

class plant_Family_dao_Impl(base_dao,plant_Family_dao):

    def __init__(self):
        self.connection = self.get_conn()

    def insert(self,PlantFamily):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Plant_Family VALUES (%s, %s,%s)",
                                (PlantFamily.id, PlantFamily.name,PlantFamily.info))
        #self.connection.commit()
        cursor.close()
    
    def update(self,PlantFamily) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("UPDATE Plant_Family SET  id=%s, name=%s,info=%s",
                                ( PlantFamily.id, PlantFamily.name,PlantFamily.info))
        #self.connection.commit()
        cursor.close()
    
    def delete(self,PlantFamilyID):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("DELETE FROM Plant_Family WHERE id=%s", (PlantFamilyID,))
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
    
    def update(self,PlantGenus) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("UPDATE Plant_Genus SET  id=%s, name=%s,info=%s",
                                ( PlantGenus.id, PlantGenus.name,PlantGenus.info))

        #self.connection.commit()
        cursor.close()
    
    def delete(self,PlantGenusID):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("DELETE FROM Plant_Genus WHERE id=%s", (PlantGenusID,))

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
    
    def update(self,PlantSpecies) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("UPDATE Plant_Species SET  id=%s, name=%s,info=%s",
                                (PlantSpecies.id, PlantSpecies.name,PlantSpecies.info))

        #self.connection.commit()
        cursor.close()
    
    def delete(self,PlantSpeciesID):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("DELETE FROM Plant_Species WHERE id=%s", (PlantSpeciesID,))

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
    
    def update(self,PlantZone) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("UPDATE Plant_Zone SET  ZoneID=%s, prov=%s,city=%s,county=%s,modified_time=%s",
                                ( PlantZone.ZoneID, PlantZone.Prov,PlantZone.City,PlantZone.County,PlantZone.modified_time))

        #self.connection.commit()
        cursor.close()
    
    def delete(self,PlantZoneID):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute("DELETE FROM Plant_Zone WHERE id=%s", (PlantZoneID,))

        #self.connection.commit()
        cursor.close()
  
    def select(self,sql) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute(sql)
        #self.connection.commit()
        cursor.close()