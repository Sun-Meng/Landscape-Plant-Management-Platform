import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("../..")
import pandas as pd
from db.DaoImpl.daoImpl_X import Monitor_dao_Impl, Monitoring_Equipment_dao_Impl, Monitoring_Personnel_dao_Impl
from db.domain.domain_X import Monitoring_Personnel

def import_csv_to_database(csv_filename):
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "plantKnit", "data", csv_filename)
    # 读取 CSV 文件
    data = pd.read_csv(csv_path, sep=',')
    monitor_dao = Monitor_dao_Impl()
    equipment_dao = Monitoring_Equipment_dao_Impl()
    personnel_dao = Monitoring_Personnel_dao_Impl()

    for index, row in data.iterrows():
        personnel = Monitoring_Personnel(
            row.tolist()[0],  # personID
            row.tolist()[1],  # name
            row.tolist()[2],  # sex
            row.tolist()[5],  # create_time
            row.tolist()[6],  # update_time
            row.tolist()[3],  # birth
            row.tolist()[4]   # tel
        )
        personnel_dao.insert(personnel)

    print(f"CSV文件 '{csv_filename}' 导入数据库成功")

if __name__ == "__main__":
    # 从终端获取用户输入的 CSV 文件名
    csv_filename = input("请输入要导入的CSV文件的名称（包括文件扩展名）：")

    import_csv_to_database(csv_filename)
