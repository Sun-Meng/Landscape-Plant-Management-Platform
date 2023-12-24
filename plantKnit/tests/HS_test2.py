import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("../..")

from db.utils.leading import import_csv_to_database
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
