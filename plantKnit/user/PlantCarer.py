import sys
sys.path.append("../..")
from db.DaoImpl.daoImpl_S import *
from db.DaoImpl.daoImpl_Y import *
from db.DaoImpl.daoImpl_X import *
from db.utils.Factor import *
class PlantCarer(object):
    def __init__(self):
        factory=DaoFactory
        self.careJob=factory.get_dao("CareJob")
        self.pestInfo=factory.get_dao("PestInfo")
        #self.workerId=

    def CareJob_lookUp(self,workerId):
        name=self.careJob.select_workerName(workerId)
        print(f"{name}'s Workplace")
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
    #根据属性HealthStatus筛选，重点在 病虫害治理相关的 表连接
    #format:
    #植物ID　植物病名　使用药剂名　药剂用量　药剂过期时间　治理措施
    def SickCaringMethod_lookUp(self,workerId,HealthStatus):
        #union+条件
        myJobs=self.pestInfo.select()
        for job in myJobs:
            print('''
                    植物id:%s ,
                    植物病名:%s, 
                    使用药剂名:%s, 
                    药剂用量:%s, 
                    药剂过期时间:%s, 
                    治理措施:%s, 
                    '''
                    %(job[0] .strip() , job[1], job[2], job[3], job[4],job[5]))
            

#上级管理部门（写在Higher类）
    #format : 任务id 任务名称 任务日期 任务地点 目标植物 植物健康状况 养护人 完成情况 完成时间