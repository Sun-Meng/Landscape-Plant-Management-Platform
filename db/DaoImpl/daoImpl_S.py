
from db.Dao.dao_S import careJob_dao, careWorker_dao, plant_Family_dao, plant_Genus_dao, plant_Species_dao, plant_Zone_dao

from db.utils.dao import base_dao

class careJob_dao_Impl(base_dao,careJob_dao):
    
    def _init__(self):
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
        cursor.execute()

        self.connection.commit()
        cursor.close()
    

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
    
    def select(self,sql) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

        self.connection.commit()
        cursor.close()

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