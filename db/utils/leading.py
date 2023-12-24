import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("../..")
import pandas as pd

def import_csv_to_database(csv_filename, dao_instance, entity_class):
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "plantKnit", "data", csv_filename)
    # 读取 CSV 文件
    data = pd.read_csv(csv_path, sep=',')

    for _, row in data.iterrows():
        list = row.tolist()

        entity_data = []
        for item in list:
            entity_data.append(item)

        # 使用可变数量的参数传递给实体类的构造函数
        entity_instance = entity_class(*entity_data)
        dao_instance.insert(entity_instance)

    print(f"CSV文件 '{csv_filename}' 导入数据库成功")

if __name__ == "__main__":
    from db.DaoImpl.daoImpl_X import Monitor_dao_Impl, Monitoring_Equipment_dao_Impl, Monitoring_Personnel_dao_Impl
    from db.domain.domain_X import Monitoring_Personnel

    # 从终端获取用户输入的 CSV 文件名
    csv_filename = input("请输入要导入的CSV文件的名称（包括文件扩展名）：")

    # 选择要使用的 DAO 实例和实体类
    dao_instance = Monitoring_Personnel_dao_Impl()  # 可根据需求选择其他实例
    entity_class = Monitoring_Personnel  # 可根据需求选择其他实体类

    # 调用通用函数
    import_csv_to_database(csv_filename, dao_instance, entity_class)
