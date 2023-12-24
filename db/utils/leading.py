import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("../..")
import pandas as pd
from db.DaoImpl.daoImpl_X import Monitor_dao_Impl, Monitoring_Equipment_dao_Impl, Monitoring_Personnel_dao_Impl
from db.domain.domain_X import Monitoring_Personnel

def import_csv_to_database(csv_path):
    # 读取 CSV 文件
    data = pd.read_csv(csv_path)

    # 使用数据库操作类进行数据库插入操作
    monitor_dao = Monitor_dao_Impl()
    equipment_dao = Monitoring_Equipment_dao_Impl()
    personnel_dao = Monitoring_Personnel_dao_Impl()

    for index, row in data.iterrows():
        personnel = Monitoring_Personnel(
            personID=row['personID'],
            name=row['name'],
            sex=row['sex'],
            create_time=row['create_time'],
            update_time=row['update_time'],
            birth=row['birth'],
            tel=row['tel']
        )

        # 执行插入操作
        personnel_dao.insert(personnel)

    print("CSV文件导入数据库成功")

if __name__ == "__main__":
    # 使用 os.path.join 构建文件路径
    current_directory = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_directory, "..", "docs", "HS.csv")
    import_csv_to_database(csv_path)
