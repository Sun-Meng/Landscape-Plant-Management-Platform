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