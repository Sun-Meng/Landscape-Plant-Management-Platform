
import sys
sys.path.append("../..")
from db.DaoImpl.daoImpl_S import careJob_dao_Impl


dao=careJob_dao_Impl()
careJobs=dao.select_all()

for job in careJobs:
    print("JobID:", job[0])
    print("WorkerID:", job[1])
    print("养护人：", job[2])
    print("养护日期：", job[3])
    print("养护地点：", job[4])
    print()