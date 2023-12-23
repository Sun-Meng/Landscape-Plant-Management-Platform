class CareJob(object):
    def __init__(self, JobID,WorkerID,Name, Date, Location,Content,Result):
        self.__JobID = JobID
        self.__Name = Name
        self.__Date = Date
        self.__Location = Location
        self.__Content=Content
        self.__Result=Result
    
    def get_JobID(self):
        return self.__JobID
    
    def get_WorkerID(self):
        return self.__WorkerID
    
    def get_Name(self):
        return self.__Name
    
    def get_Date(self):
        return self.__Date
    
    def get_Location(self):
        return self.__Location
    
    def get_Content(self):
        return self.__Content
    
    def get_Result(self):
        return self.__Result
    
    #任务导入的时候就可以先完成【表连接】操作，这样直接读入的就是任务内容，根据条件进行筛选即可

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
    
    def checkCareJob(ID,job):
        #需要连接 养护任务表 和 养护人信息表
        job.set_workerID()
        #养护人员只提供workerID