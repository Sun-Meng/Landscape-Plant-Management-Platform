import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("../..")
from db.DaoImpl.daoImpl_S import *
from db.DaoImpl.daoImpl_Y import *
from db.DaoImpl.daoImpl_X import *
from db.domain.domain_Y import *
from db.domain.domain_S import *
from db.domain.domain_X import *
from db.utils.loading import import_csv_to_database
from plantKnit.user.Higher import *
from db.DaoImpl.daoImpl_X import Monitor_dao_Impl, Monitoring_Equipment_dao_Impl, Monitoring_Personnel_dao_Impl

user=Higher()
userID=233           #对应数据里的 刘立
#测试数据
#查询个人养护任务（1）
user.viewCare(userID)







'''
import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("../..")

from db.utils.loading import import_csv_to_database
from db.DaoImpl.daoImpl_X import Monitoring_Personnel_dao_Impl
from db.domain.domain_X import Monitoring_Personnel

def main():
    dao_instance = Monitoring_Personnel_dao_Impl()  # 可根据需求选择其他实例
    entity_class = Monitoring_Personnel  # 可根据需求选择其他实体类
    csv_filename = input("请输入要导入的 CSV 文件的名称（包括文件扩展名）：")
    
    # 调用通用函数
    import_csv_to_database(csv_filename, dao_instance, entity_class)

if __name__ == "__main__":
    main()
'''

'''
import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("../..")
from db.DaoImpl.daoImpl_X import Monitoring_Personnel_dao_Impl

dao=Monitoring_Personnel_dao_Impl()
Monitoring_Personnel=dao.select()

for job in Monitoring_Personnel:
    print("personID:", job[0])
    print("姓名:", job[1])
    print("性别：", job[2])
    print("出生日期：", job[3])
    print("电话号码：", job[4])
    print("创建时间：", job[5])
    print("更新时间：", job[6])
    print()
'''