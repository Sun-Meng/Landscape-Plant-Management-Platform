from db.Dao.dao_X import Monitor_dao, Monitoring_Equipment_dao, Monitoring_Personnel_dao

from db.utils.dao import base_dao

class Monitor_dao_Impl(base_dao,Monitor_dao):
    
    def _init__(self):
        self.connection = self.get_conn()

    def insert(self,Monitor) :
        cursor = self.connection.cursor()
        cursor.execute("insert into Monitor values(%s,%s,%s,%s)",(Monitor.diseaseID,Monitor.name,Monitor.create_time,Monitor.update_time))
        self.connection.commit()
        cursor.close()

    def delete(self,Monitor):
        cursor = self.connection.cursor()
        cursor.execute("delete from Monitor where diseaseID=%s",(Monitor.diseaseID))
        self.connection.commit()
        cursor.close()
    
    def update(self,Monitor):
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


class Monitoring_Equipment_dao_Impl(base_dao,Monitoring_Equipment_dao):
    
    def _init__(self):
        self.connection = self.get_conn()

    def insert(self,Monitoring_Equipment) :
        cursor = self.connection.cursor()
        cursor.execute("insert into Monitoring_Equipment values(%s,%s,%s,%s)",(Monitoring_Equipment.id,Monitoring_Equipment.time,Monitoring_Equipment.place,Monitoring_Equipment.object))
        self.connection.commit()
        cursor.close()

    def delete(self,Monitoring_Equipment):
        cursor = self.connection.cursor()
        cursor.execute("delete from Monitoring_Equipment where id=%s",(Monitoring_Equipment.id))
        self.connection.commit()
        cursor.close()
    
    def update(self,Monitoring_Equipment):
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


class Monitoring_Personnel_dao_Impl(base_dao,Monitoring_Personnel_dao):
    
    def _init__(self):
        self.connection = self.get_conn()

    def insert(self,Monitoring_Personnel) :
        cursor = self.connection.cursor()
        cursor.execute("insert into Monitoring_Personnel values(%s,%s,%s,%s)",(Monitoring_Personnel.id,Monitoring_Personnel.name,Monitoring_Personnel.sex,Monitoring_Personnel.create_time,Monitoring_Personnel.update_time,Monitoring_Personnel.birth,Monitoring_Personnel.tel))
        self.connection.commit()
        cursor.close()

    def delete(self,Monitoring_Personnel):
        cursor = self.connection.cursor()
        cursor.execute("delete from Monitoring_Personnel where id=%s",(Monitoring_Personnel.id))
        self.connection.commit()
        cursor.close()
    
    def update(self,Monitoring_Personnel):
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