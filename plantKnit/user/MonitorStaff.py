import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("../..")
from db.daoImpl import *
from db.utils.Factor import *
from db.utils.loading import import_csv_to_database
class MonitorStaff(object):
    def __init__(self):
        factory=DaoFactory
        self.Monitor=factory.get_dao("Monitor")
    
    def logging(self):
        dao_instance = Monitor_dao_Impl()
        entity_class = Monitor

        data_list = []
        header = "resultID,PlantID,equipmentID,HealthStatus,name,create_time,update_time,temp,acid"
        print(f"请按照以下格式逐行输入数据（输入 'quit' 结束录入）:\n{header}")

        # 存储异常数据的列表
        invalid_data_list = []

        while True:
            input_data = input("请输入数据：")
            if input_data.lower() == "quit":
                break
            data_list.append(input_data)

        # 将手动输入的数据导入数据库
        for data in data_list:
            # 分割输入的数据为列表
            data_as_list = data.split(',')

            # 使用可变数量的参数传递给实体类的构造函数
            entity_instance = entity_class(*data_as_list)

            # 检查temp和acid是否在指定范围内
            temp_valid = -273 <= float(entity_instance.temp) <= 1000
            acid_valid = 0 <= float(entity_instance.acid) <= 14

            if not temp_valid or not acid_valid:
                # 存储异常数据到列表
                invalid_data_list.append(data)
                # 输出存储失败的消息
                print("存储失败：输入数据超出范围")
            else:
                # 数据符合范围，将数据插入数据库
                dao_instance.insert(entity_instance)
                print("手动输入的数据导入数据库成功")
            
            if invalid_data_list:
            # 拼接上级文件夹的log文件夹路径
                log_folder_path = "../log"
                error_file_path = f"{log_folder_path}/error.txt"

                with open(error_file_path, "w") as file:
                    file.write("以下数据超出范围，未存入数据库：\n")
                    for invalid_data in invalid_data_list:
                        file.write(invalid_data + "\n")
                print("异常数据已存储到文件 error.txt 中")

    
    def loading(self):
        dao_instance = Monitor_dao_Impl()
        entity_class = Monitor
        csv_filename = input("请输入要导入的 CSV 文件的名称（包括文件扩展名）：")
    
        # 调用通用函数
        import_csv_to_database(csv_filename, dao_instance, entity_class)
        
    def query_average_temp(self):
        dao_instance = Monitor_dao_Impl()
        average = dao_instance.calculate_average_temp()
        if average is not None:
            print(f"平均值为: {average}")
        else:
            print("无法计算平均值，数据为空或不可用")

    def query_max_temp(self):
        dao_instance = Monitor_dao_Impl()
        max = dao_instance.find_max_temp()
        if max is not None:
            print(f"最大值为: {max}")
        else:
            print("无法找到最大值，数据为空或不可用")
            
    def query_min_temp(self):
        dao_instance = Monitor_dao_Impl()
        min = dao_instance.find_min_temp()
        if min is not None:
            print(f"最小值为: {min}")
        else:
            print("无法找到最大值，数据为空或不可用")
            
    def query_average_acid(self):
        dao_instance = Monitor_dao_Impl()
        average = dao_instance.calculate_average_acid()
        if average is not None:
            print(f"平均值为: {average}")
        else:
            print("无法计算平均值，数据为空或不可用")

    def query_max_acid(self):
        dao_instance = Monitor_dao_Impl()
        max = dao_instance.find_max_acid()
        if max is not None:
            print(f"最大值为: {max}")
        else:
            print("无法找到最大值，数据为空或不可用")
            
    def query_min_acid(self):
        dao_instance = Monitor_dao_Impl()
        min = dao_instance.find_min_acid()
        if min is not None:
            print(f"最小值为: {min}")
        else:
            print("无法找到最大值，数据为空或不可用")

    
    def menu(self):
        while(True):
            print('-----监测人员界面-----')
            print('1.手工录入数据')
            print('2.批量导入数据')
            print('3.查询监测表的数据中植物温度的平均值，最大值，最小值')
            print('4.查询监测表的数据中土壤酸度的平均值，最大值，最小值')
            print('5.结束')
            i=input('所执行业务ID:')
            if(i=="1"):
                self.logging()
            elif(i=="2"):
                self.loading()
            elif i == "3":
                self.query_average_temp()
                self.query_max_temp()
                self.query_min_temp()
            elif i == "4":
                self.query_average_acid()
                self.query_max_acid()
                self.query_min_acid()
            elif i == "5":
                    break
            else:
                print('错误的执行ID')