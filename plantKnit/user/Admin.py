import sys
sys.path.append("../..")
from db.utils.loading import import_csv_to_database
from db.daoImpl import *
from db.utils.Factor import *
from datetime import datetime
class Admin(base_dao):
    def __init__(self):
        factor=DaoFactory
        self.plants=factor.get_dao("Plants")
        self.family=factor.get_dao("Plant_Family")
        self.genus=factor.get_dao("Plant_Genus")
        self.species=factor.get_dao("Plant_Species")
        self.zone=factor.get_dao("Plant_Zone")
        self.connection = self.get_conn() 
    def viewPlant(self,id):
        temp=self.plants.select(id)
        if(temp!=None):
            print(vars(temp))
        else:print("id有误")
    def viewAllPlants(self):
        temp=self.plants.selectAll()
        for i in temp:
            print(i)
    def viewSort(self,id):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT 
                    Plants.Name, 
                    Plant_Family.name AS FamilyName, Plant_Family.info AS FamilyInfo,
                    Plant_Genus.name AS GenusName, Plant_Genus.info AS GenusInfo,
                    Plant_Species.name AS SpeciesName, Plant_Species.info AS SpeciesInfo,
                    Plant_Zone.prov, Plant_Zone.city, Plant_Zone.county
                FROM 
                    Plants
                INNER JOIN 
                    Plant_Family ON Plants.FamilyID = Plant_Family.id
                INNER JOIN 
                    Plant_Genus ON Plants.GenusID = Plant_Genus.id
                INNER JOIN 
                    Plant_Species ON Plants.SpeciesID = Plant_Species.id
                INNER JOIN 
                    Plant_Zone ON Plants.ZoneID = Plant_Zone.ZoneID
                WHERE 
                    Plants.PlantID = %s
            ''', (id,))
            result = cursor.fetchone()
            # 打印结果
            print(result)
            return True
        except Exception as e:
            print(e)
            return False
    def updateFamily(self,family):
        self.family.update(family)
    def updatePlants(self,plant):
        self.plants.update(plant)
    def updateGenus(self,genus):
        self.genus.update(genus)
    def updateSpecies(self,species):
        self.species.update(species)
    def updateZone(self,zone):
        self.zone.update(zone)
    def count_plants_by_family_id(self, family_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT name FROM Plant_Family WHERE id = %s", (family_id))
        result =cursor.fetchone()
        view_name="Family_"+result[0] if result else print("Erro ID")
        cursor.execute(f"SELECT name FROM master WHERE type='view' AND name='{view_name}'")
        result = cursor.fetchone()
        if not result:
            cursor.execute(f"CREATE VIEW {view_name} AS SELECT * FROM Plants")
            cursor.execute("CREATE VIEW "+view_name+" AS SELECT * FROM Plants WHERE FamilyID = %s", (family_id))
        cursor.execute("SELECT COUNT(*) FROM "+view_name, (family_id))
        result = cursor.fetchone()
        print(result) if result[0] else print("None")
        
    def query_plants_by_attributes(self, attributes):
        cursor = self.connection.cursor()
        query = "SELECT * FROM Plants WHERE " + " AND ".join(f"{key} = %s" for key in attributes.keys())
        values = tuple(attributes.values())
        cursor.execute(query, values)
        results = cursor.fetchall()
        print(results)
    def setConfigInfo(self):
         while(True):
            print('-----系统信息配置界面-----')
            print('1.配置植物信息')
            print('2.配置植物分类信息')
            print('3.配置植物养护信息')
            print('4.配置植物病虫害信息')
            print('5.配置植物监测信息')
            print('6.配置系统用户信息')
            print('7.退出系统配置')
            i=input('所执行业务ID:')
            if(i=="1"):
                import_csv_to_database("Plants.csv", PlantsDaoImpl(), Plants)
            elif(i=="2"):
                import_csv_to_database("PlantFamily.csv", plant_Family_dao_Impl(), PlantFamily)
                import_csv_to_database("PlantGenus.csv", plant_Genus_dao_Impl(), PlantGenus)
                import_csv_to_database("PlantSpecies.csv", plant_Species_dao_Impl(), PlantSpecies)
                import_csv_to_database("PlantZone.csv", plant_Zone_dao_Impl(), PlantZone)
            elif(i=="3"):
                import_csv_to_database("careWorker.csv",careWorker_dao_Impl(), CareWorker)
                import_csv_to_database("careJob.csv",careJob_dao_Impl(), CareJob)
            elif(i=="4"):
                import_csv_to_database("pestInfo.csv",PestInfoDaoImpl(),PestInfo)
                import_csv_to_database("medicines.csv",MedicinesDaoImpl(),Medicines)
                import_csv_to_database("prevent.csv",PreventDaoImpl(),Prevent)
                import_csv_to_database("usage.csv",UsageDaoImpl(),Usage)
            elif(i=="5"):
                import_csv_to_database("Monitoring_Personnel.csv",Monitoring_Personnel_dao_Impl(), Monitoring_Personnel)
                import_csv_to_database("Monitoring_Equipment.csv",Monitoring_Equipment_dao_Impl(), Monitoring_Equipment)
            elif(i=="6"):
                import_csv_to_database("user.csv",user_dao_Impl(),User)
            elif(i=="7"):
                break
            else:
                print('错误的执行ID')

    def menu(self):
        while(True):
            print('-----管理员界面-----')
            print('1.查看植物信息')
            print('2.查看所有植物信息')
            print('3.查看植物分类信息')
            print('4.修改植物信息')
            print('5.修改科信息')
            print('6.修改属信息')
            print('7.修改种信息')
            print('8.修改区域信息')
            print('9.系统信息配置')
            print('10.查询科内植物数量')
            print('11.根据任意属性查询符合的植物信息')
            print('12.结束')
            i=input('所执行业务ID:')
            if(i=="1"):
                self.viewPlant(input('植物ID:'))
            elif(i=="2"):
                self.viewAllPlants()
            elif(i=="3"):
                self.viewSort(input('植物ID:'))
            elif(i=="4"):
                plants=Plants(input('植物ID:'),input('植物名:'),input('别名:'),input('形态特征:'),input('栽培技术要点:'),input('应用价值:'),input('植物介绍:'),input('创建人员:'),input('科ID:'),input('属ID:'),input('种ID:'),input('区域ID:'),datetime.now(),datetime.now())
                self.plants.update(plants)
            elif(i=="5"):
                family=PlantFamily(input('科ID:'),input('科名:'),input('科描述:'))
                if(self.family.update(family)):
                    print("科信息更新成功！")
                    print()
                else:
                    break
            elif(i=="6"):
                genus=PlantGenus(input('种ID:'),input('种名:'),input('种描述:'))
                if(self.genus.update(genus)):
                    print("种信息更新成功！")
                    print()
                else:
                    break
            elif(i=="7"):
                species=PlantSpecies(input('属ID:'),input('属名:'),input('属描述:'))
                if(self.species.update(species)):
                    print("类信息更新成功！")
                    print()
                else:
                    break
            elif(i=="8"):
                zone=PlantZone(input('区域id:'),input('省：'),input('市：'),input('县/乡：'),datetime.now(),datetime.now())
                if(self.zone.update(zone)):
                    print("分布区域信息更新成功！")
                    print()
                else:
                    break
            elif(i=="9"):
                self.setConfigInfo()
            elif(i=="10"):
                self.count_plants_by_family_id(input("科ID："))
            elif(i=="11"):
                attributes = {}
                attribute_names = ['PlantID', 'Name', 'Alias', 'MorphologicalFeatures', 'CultivationKeyPoints', 'ApplicationValue', 'PlantIntroduction', 'Creator', 'CreationTime', 'UpdateTime', 'FamilyID', 'GenusID', 'SpeciesID', 'ZoneID']
                while True:
                    print("请选择一个属性：")
                    for i, attribute_name in enumerate(attribute_names):
                        if attribute_name in attributes:
                            continue
                        print(f"{i}. {attribute_name}")
                    attribute_index = input("请输入属性的序号（输入'q'结束输入）：")
                    if attribute_index.lower() == 'q':
                        break
                    attribute_name = attribute_names[int(attribute_index)]
                    attribute_value = input(f"请输入属性'{attribute_name}'的值：")
                    attributes[attribute_name] = attribute_value
                self.query_plants_by_attributes(attributes)
            elif(i=="12"):
                break
            else:
                print('错误的执行ID')
    
