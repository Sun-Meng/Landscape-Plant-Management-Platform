import sys
sys.path.append("../..")
from db.DaoImpl.daoImpl_S import *
from db.DaoImpl.daoImpl_Y import *
from db.DaoImpl.daoImpl_X import *
from db.utils.Factor import *
class PlantCarer(object):
    def __init__(self,workerId):
        factory=DaoFactory
        self.careJob=factory.get_dao("CareJob")
        self.prevent=factory.get_dao("Prevent")
        self.workerId=workerId

    def CareJob_lookUp(self):
        name=self.careJob.select_workerName(self.workerId)
        print(f"{name}'s Workplace")
        myJobs=self.careJob.select_by_id(self.workerId)
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
                  %(job[0], job[1], job[2], job[3], job[4],job[5],job[6],job[7]))
        
    #病虫害防治措施单独查询即可
    #根据属性HealthStatus筛选，重点在 病虫害治理相关的 表连接
    #format:
    #植物ID　植物病名　使用药剂名　药剂用量　药剂过期时间　治理措施
    def CaringMethod_lookUp(self,HealthStatus):
        #筛选出该养护人员任务列表中生病的植物，得到PlantID
        #根据PlantID，查prevent,获得相关的病虫害治理措施
        myJobs=self.prevent.select_by_id(self.workerId,HealthStatus)
        for job in myJobs:
            print('''
                    植物id:%s ,
                    植物名称:%s,
                    植物病名:%s, 
                    使用药剂名:%s, 
                    药剂用量:%s, 
                    药剂过期时间:%s, 
                    治理措施:%s, 
                    '''
                    %(job[0], job[1], job[2], job[3], job[4],job[5],job[6]))
    def menu(self):
        while(True):
            print('-----养护人员界面-----')
            print('1.查看个人养护任务信息')
            print('2.结束')
            i=input('所执行业务ID:')
            if(i==1):
                self.CareJob_lookUp()
            elif(i==2):
                break
            else:
                print('错误的执行ID')  

#上级管理部门（写在Higher类）
    #format : 任务id 任务名称 任务日期 任务地点 目标植物 植物健康状况 养护人 完成情况 完成时间