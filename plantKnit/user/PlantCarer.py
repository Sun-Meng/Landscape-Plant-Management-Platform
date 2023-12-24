import sys
sys.path.append("../..")
from db.DaoImpl.daoImpl_S import *
from db.DaoImpl.daoImpl_Y import *
from db.DaoImpl.daoImpl_X import *
from db.utils.Factor import *
class PlantCarer(object):
    def __init__(self):
        factory=DaoFactory()
        self.careJob=factory.get_dao("CareJob")

    def CareJob_lookUp(self,workerId):
        name=self.careJob.select_workerName(workerId)
        print("%s 's Workplace",(name,))
        myJobs=self.careJob.select_by_id(workerId)
        for job in myJobs:
            print('''
                    任务id:%s ,
                    任务名称:%s, 
                    任务日期:%s, 
                    任务地点:%s, 
                    目标植物:%s, 
                    植物健康状况:%s, 
                    一般养护措施:%s, 
                    完成情况:%s
                  '''
                  %(job[0] .strip() , job[1], job[2], job[3], job[4],job[5],job[6],job[7]))
        
    #病虫害防治措施单独查询即可