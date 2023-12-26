import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("../..")
from db.daoImpl import *
from db.utils.Factor import *
class HigherManager(base_dao):
    def __init__(self):
        factory=DaoFactory
        self.careJob=factory.get_dao("CareJob")
        self.careWorker=factory.get_dao("CareWorker")
        self.Monitoring_Personnel=factory.get_dao("Monitoring_Personnel")
        self.connection = self.get_conn() 
     
    def viewCare(self):
        CareResult='''
            SELECT JobID,JobTitle,date,location,p.Name,HealthStatus,worker_name,result,
            FROM CareJob as job 
                inner join CareWorker as cw on job.workerID=cw.workerID
                inner join Plants as p on p.PlantID=job.PlantID
                inner join Monitor as m on m.PlantID=p.PlantID 
        '''
        results=self.careJob.select(CareResult)
        if(results!=None):
            for res in results:
                print('''
                        任务id:%s ,
                        任务名称:%s,
                        任务日期:%s, 
                        任务地点:%s, 
                        目标植物:%s, 
                        植物健康状况:%s, 
                        养护人:%s, 
                        完成情况:%s,
                        '''
                        %(res[0], res[1], res[2], res[3], res[4],res[5],res[6],res[7])) 
                print()
        else: print("没有找到养护结果信息")
    # ID, Name, Sex, Birth, Tel,create_time,modified_time
    def viewCareWorker(self):
        results=self.careJob.select_all()
        if(results!=None):
            for res in results:
                print('''
                        人员id:%s ,
                        人员名称:%s,
                        人员性别:%s, 
                        人员出生日期:%s, 
                        人员联系电话:%s, 
                        '''
                        %(res[0], res[1], res[2], res[3], res[4])) 
                print()
        else: print("没有找到养护人员信息")
        
    def viewMonitoring_Personnel(self,id):
        temp=self.Monitoring_Personnel.select(id)
        if(temp!=None):
            for i in temp:
                print(i)
        else:print("id有误")
        
    def combineSearch(self,id):
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT 
                CareJob.PlantID,
                CareJob.workerID,
                CareJob.JobID,
                CareJob.JobTitle,
                CareJob.RegularJob,
                CareJob.result,
                CareJob.date,
                CareJob.location,
                CareJob.create_time,
                CareJob.modified_time,
                Plants.Name AS PlantName,
                Plants.Alias,
                Plants.MorphologicalFeatures,
                Plants.CultivationKeyPoints,
                Plants.ApplicationValue,
                Plants.PlantIntroduction,
                Plants.Creator,
                Plants.CreationTime,
                Plants.UpdateTime,
                Plants.FamilyID,
                Plant_Family.PlantID AS FamilyID,
                Plant_Family.name AS FamilyName,
                Plant_Family.info AS FamilyInfo,
                Plant_Genus.PlantID AS GenusID,
                Plant_Genus.name AS GenusName,
                Plant_Genus.info AS GenusInfo,
                Plant_Species.PlantID AS SpeciesID,
                Plant_Species.name AS SpeciesName,
                Plant_Species.info AS SpeciesInfo
            FROM 
                CareJob
            JOIN 
                Plants ON CareJob.PlantID = Plants.PlantID
            JOIN 
                Plant_Family ON CareJob.PlantID = Plant_Family.PlantID
            JOIN 
                Plant_Genus ON Plants.GenusID = Plant_Genus.PlantID
            JOIN 
                Plant_Species ON Plants.SpeciesID = Plant_Species.id
            WHERE 
                CareJob.PlantID = (%s);
            ''', (id,))
        result = cursor.fetchone()
        print(result)
    
    def menu(self):
        while(True):
            print('-----上层管理部门界面-----')
            print('1.查看养护结果')
            print('2.查看工作人员信息')
            print('3.查看植物的所有养护、分类、基本信息')
            print('4.结束')
            i=input('所执行业务ID：')
            if(i=="1"):
                self.viewCare()
            elif(i=="2"):
                print('-----查看工作人员信息-----')
                print('1.查看养护人员信息')
                print('2.查看监测人员信息')
                print('3.结束')
                j=input('所执行业务ID：')
                if(j=="1"):
                    self.viewCareWorker()
                elif(j=="2"):
                    self.viewMonitoring_Personnel(input('请输入要查询的人员ID：'))
                elif(j=="3"):
                    break
                else:
                    print('错误的执行ID')
            elif(i=="3"):
                self.combineSearch(input('请输入要查询的植物ID:'))
            elif(i=="4"):
                break
            else:
                print('错误的执行ID')
                