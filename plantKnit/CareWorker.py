class CareWorker(object):
    def __init__(self, ID, Name, Sex, Age, Tel):
        self.__ID = ID
        self.__Name = Name
        self.__Sex = Sex
        self.__Age = Age
        self.__Tel = Tel

    def get_ID(self):
        return self.__ID

    def get_Name(self):
        return self.__Name

    def get_Sex(self):
        return self.__Sex
    
    def get_Age(self):
        return self.__Age
    
    def get_Tel(self):
        return self.__Tel
    
    def checkCareJob(self):
        #需要连接 养护任务表 和 养护人信息表
        #这里直接return(先import CareJob.py)
        #呈现的为实体，还没有联系到表的连接上
