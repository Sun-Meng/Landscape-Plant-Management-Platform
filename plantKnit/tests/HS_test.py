import sys
import os
# 将当前工作目录设置为项目根目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("../..")
from db.DaoImpl.daoImpl_X import Monitoring_Personnel_dao_Impl

dao=Monitoring_Personnel_dao_Impl()
Monitoring_Personnel=dao.select_all()

for job in Monitoring_Personnel:
    print("personID:", job[0])
    print("姓名:", job[1])
    print("性别：", job[2])
    print("出生日期：", job[3])
    print("电话号码：", job[4])
    print("创建时间：", job[5])
    print("更新时间：", job[6])
    print()