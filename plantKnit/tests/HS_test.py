import sys
sys.path.append("../..")
from db.DaoImpl.daoImpl_X import Monitoring_Personnel_dao_Impl


dao=Monitoring_Personnel_dao_Impl()
Monitoring_Personnel=dao.select_all()

for job in Monitoring_Personnel:
    print("JobID:", job[0])
    print("WorkerID:", job[1])
    print("养护人：", job[2])
    print("养护日期：", job[3])
    print("养护地点：", job[4])
    print()