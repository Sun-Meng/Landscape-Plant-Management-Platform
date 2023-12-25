import sys
sys.path.append("../..")

import pandas as pd

from db.domain.domain_X import *

from db.Dao.dao_X import Monitor_dao, Monitoring_Equipment_dao, Monitoring_Personnel_dao

from db.utils.dao import *

class Monitor_dao_Impl(base_dao,Monitor_dao):
    
    def __init__(self):
        self.connection = self.get_conn()

    def insert(self,Monitor) :
        cursor = self.connection.cursor()
        cursor.execute("insert into Monitor values(%s,%s,%s,%s)",(Monitor.resultID,Monitor.name,Monitor.create_time,Monitor.update_time))
        self.connection.commit()
        cursor.close()

    def delete(self,Monitor):
        cursor = self.connection.cursor()
        cursor.execute("delete from Monitor where resultID=%s",(Monitor.resultID))
        self.connection.commit()
        cursor.close()
    
    def update(self,Monitor):
        cursor = self.connection.cursor()
        cursor.execute("update Monitor set name = %s, create_time = %s, update_time = %s where resultID = %s",(Monitor.name, Monitor.create_time, Monitor.update_time, Monitor.resultID))
        self.connection.commit()
        cursor.close()

    def select(self,resultID):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Monitor WHERE resultID=%s", (resultID,))
        result = cursor.fetchall()
        cursor.close()
        return result


class Monitoring_Equipment_dao_Impl(base_dao,Monitoring_Equipment_dao):
    
    def __init__(self):
        self.connection = self.get_conn()

    def insert(self,Monitoring_Equipment) :
        cursor = self.connection.cursor()
        cursor.execute("insert into Monitoring_Equipment values(%s,%s,%s,%s)",(Monitoring_Equipment.equipmentID,Monitoring_Equipment.time,Monitoring_Equipment.place,Monitoring_Equipment.object))
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
        cursor.execute("SELECT * FROM Monitoring_Equipment WHERE equipmentID=%s", (equipmentID,))
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
        cursor.execute("SELECT * FROM Monitoring_Personnel WHERE PersonID=%s", (PersonID,))
        result = cursor.fetchall()
        print(pd.DataFrame(list(result)).shape)
        cursor.close()
        return result
    
    def select_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Monitoring_Personnel")
        results = cursor.fetchall()
        print(pd.DataFrame(list(results)).shape)
        cursor.close()
        return results