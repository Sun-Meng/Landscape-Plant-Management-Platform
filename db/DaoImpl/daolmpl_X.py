from db.Dao.dao_X import Monitor_dao, Monitoring_Equipment_dao, Monitoring_Personnel_dao

from db.utils.dao import base_dao

class Monitor_dao_Impl(base_dao,Monitor_dao):
    
    def _init__(self):
        self.connection = self.get_conn()

    def insert(self,Monitor) :
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

        self.connection.commit()
        cursor.close()

    def delete(self,Monitor):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

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
        #插入sql
        cursor.execute()

        self.connection.commit()
        cursor.close()

    def delete(self,Monitoring_Equipment):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

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
        #插入sql
        cursor.execute()

        self.connection.commit()
        cursor.close()

    def delete(self,Monitoring_Personnel):
        cursor = self.connection.cursor()
        #插入sql
        cursor.execute()

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