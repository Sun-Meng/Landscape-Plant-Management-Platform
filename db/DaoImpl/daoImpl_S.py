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
        cursor.execute()

        self.connection.commit()
        cursor.close()

    def delete(self,CareJob):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

        self.connection.commit()
        cursor.close()
    
    def update(self,CareJob):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

        self.connection.commit()
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
        cursor.execute()

        self.connection.commit()
        cursor.close()
    
    def update(self,CareWorker) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

        self.connection.commit()
        cursor.close()
   
    def delete(self,CareWorker):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

        self.connection.commit()
        cursor.close()
    
    # def select(self) :
    #     cursor = self.connection.cursor()
    #     #插入sql
    #     cursor.execute()

    #     self.connection.commit()
    #     cursor.close()


   

class plant_Family_dao_Impl(base_dao,plant_Family_dao):
    
    def insert(self,PlantFamily):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

        self.connection.commit()
        cursor.close()
    
    def update(self,PlantFamily) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

        self.connection.commit()
        cursor.close()
    
    def delete(self,PlantFamily):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

        self.connection.commit()
        cursor.close()
  
    def select(self,sql) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

        self.connection.commit()
        cursor.close()

class plant_Genus_dao_Impl(base_dao,plant_Genus_dao):
   
    def insert(self,PlantGenus):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

        self.connection.commit()
        cursor.close()
   
    def update(self,PlantGenus) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

        self.connection.commit()
        cursor.close()

    def delete(self,PlantGenus):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

        self.connection.commit()
        cursor.close()

    def select(self,sql) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

        self.connection.commit()
        cursor.close()

class plant_Species_dao_Impl(base_dao,plant_Species_dao):

    def insert(self,PlantSpecies):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

        self.connection.commit()
        cursor.close()
 
    def update(self,PlantSpecies) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

        self.connection.commit()
        cursor.close()

    def delete(self,PlantSpecies):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

        self.connection.commit()
        cursor.close()

    def select(self,sql) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

        self.connection.commit()
        cursor.close()

class plant_Zone_dao_Impl(base_dao,plant_Zone_dao):
    def insert(self,PlantZone):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

        self.connection.commit()
        cursor.close()
  
    def update(self,PlantZone) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

        self.connection.commit()
        cursor.close()
  
    def delete(self,PlantZone):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

        self.connection.commit()
        cursor.close()
    
    def select(self,sql) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

        self.connection.commit()
        cursor.close()