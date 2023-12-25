import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import sys
sys.path.append("../..")
from db.DaoImpl.daoImpl_Y import *
from db.domain.domain_Y import *
from db.domain.domain_S import *
from db.utils.loading import import_csv_to_database
from plantKnit.user.PlantCarer import *
from db.DaoImpl.daoImpl_S import careJob_dao_Impl, careWorker_dao_Impl

user=PlantCarer()
userID=233           #对应数据里的 刘立
#测试数据
import_csv_to_database("careWorker.csv",careWorker_dao_Impl(), CareWorker)
import_csv_to_database("careJob.csv",careJob_dao_Impl(), CareJob)
import_csv_to_database("pestInfo.csv",PestInfoDaoImpl(),PestInfo)
import_csv_to_database("prevent.csv",PreventDaoImpl(),Prevent)
import_csv_to_database("usage.csv",UsageDaoImpl(),Usage)
import_csv_to_database("medicines.csv",MedicinesDaoImpl(),Medicines)
#查询个人养护任务（1）
user.CareJob_lookUp(userID)

##查询有病害植物的养护措施（1.1）




# dao=careJob_dao_Impl()
# search_all='''
#     SELECT * FROM CareJob
# '''
# search_caring_info='''
#             SELECT JobID,JobTitle,worker_name,result 
#             FROM CareJob as job inner join CareWorker as worker on job.workerID=worker.workerID
#         '''
# careJobs=dao.select(search_all)

# #验证是否能从数据库中，查询所有的养护任务信息
# for job in careJobs:
#     print("JobID:", job[0])
#     print("WorkerID:", job[1])
#     print("养护日期：", job[2])
#     print("养护地点：", job[3])
#     print("养护人：", job[4])
#     print()

# #验证是否能在数据库中，根据养护人员的ID 来查询某个工作人员的任务信息
# #写select_by_workerID()
# userId=1234
# myJobs=dao.select_by_id(userId)
# for job in myJobs:
#     print("JobID:", job[0])
#     print("JobTitle:", job[1])
#     print("养护日期：", job[2])
#     print("养护地点：", job[3])
#     print("养护人：", job[4])
#     print("植物：", job[5])
#     print("养护结果：", job[6])
#     print()
    
#     print("任务id:%s ,任务名称:%s, 任务日期:%s, 任务地点:%s, 目标植物:%s, 植物健康状况:%s, 一般养护措施:%s, 病虫害防治措施:%s, 完成情况:%s"%(row[0] .strip() , row[1], row[2]))
  
    #思考过程
    #个人任务的创建(多表连接)
    #养护任务=对监测到的 有病害的植物 进行 针对性养护
    #insert的使用

    #细化：养护任务一览表-查询具体任务内容（例如，查询无病害/有病害的植物的）-防治措施
    #养护人员 查询个人任务的业务
    #（养护人员信息表 ~ 养护任务表 ~ 植物表 ~ 监测结果表 ~ 病虫害相关表（措施））
    #format : 任务id 任务名称 任务日期 任务地点 目标植物 植物健康状况 一般养护措施 病害防治措施 完成情况
    #查全部
    #查有病害的
    #查未完成的
    #查已完成的
    
    #上级管理部门
    #format : 任务id 任务名称 任务日期 任务地点 目标植物 植物健康状况 养护人 完成情况 完成时间


    #如果病虫害防治单独作为一个业务：监测有病害，查询治理措施（药剂使用 等等）

    #数据导入：loadData()--完成数据库表（按名导入）的内容导入操作
    #input:表名.csv
    #output:配置成功/失败


    