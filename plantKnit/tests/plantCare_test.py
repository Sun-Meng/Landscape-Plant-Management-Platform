
import sys
sys.path.append("../..")
from db.DaoImpl.daoImpl_S import careJob_dao_Impl


dao=careJob_dao_Impl()
search_all='''
    SELECT * FROM CareJob
'''
search_caring_info='''
            SELECT JobID,JobTitle,worker_name,result 
            FROM CareJob as job inner join Gardener as gd on job.workerID=gd.workerID
        '''
careJobs=dao.select(search_all)

#验证是否能从数据库中，查询所有的养护任务信息
for job in careJobs:
    print("JobID:", job[0])
    print("WorkerID:", job[1])
    print("养护日期：", job[2])
    print("养护地点：", job[3])
    print("养护人：", job[4])
    print()

#验证是否能在数据库中，根据养护人员的ID 来查询某个工作人员的任务信息
#写select_by_workerID()
id=?
myJobs=dao.select(id)
for job in myJobs:
    print("JobID:", job[0])
    print("JobTitle:", job[1])
    print("养护日期：", job[2])
    print("养护地点：", job[3])
    print("养护人：", job[4])
    print("植物：", job[5])
    print("养护结果：", job[6])
    print()
    
    #个人任务的创建(多表连接)
    #养护任务=对监测到的 有病害的植物 进行 针对性养护
    #insert的使用

    #细化：养护任务一览表-查询具体任务内容（例如，查询无病害/有病害的植物的）-防治措施

    #如果病虫害防治单独作为一个业务：监测有病害，查询治理措施（药剂使用 等等）
