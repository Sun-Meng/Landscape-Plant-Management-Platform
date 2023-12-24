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
