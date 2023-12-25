import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("../..")
from db.DaoImpl.daoImpl_S import *
from db.DaoImpl.daoImpl_Y import *
from db.DaoImpl.daoImpl_X import *
from db.utils.Factor import *
from db.utils.loading import import_csv_to_database
class Monitor(object):
    def __init__(self):
        factory=DaoFactory()
        self.Monitor=factory.get_Dao("Monitor")
    
    def logging(self):
        pass
    
    def loading(self):
        dao_instance = Monitoring_Personnel_dao_Impl()
        entity_class = Monitoring_Personnel
        csv_filename = input("请输入要导入的 CSV 文件的名称（包括文件扩展名）：")
    
        # 调用通用函数
        import_csv_to_database(csv_filename, dao_instance, entity_class)
    
    def menu():
        while(True):
            print('-----监测人员界面-----')
            print('1.手工录入数据')
            print('2.批量导入数据')
            print('3.结束')
            i=input('所执行业务ID：')
            if(i==1):
                logging(input('请输入数据'))
            elif(i==2):
                loading(input('%s'))
            elif(i==3):
                break
            else:
                print('错误的执行ID')