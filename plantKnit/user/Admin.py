import sys
sys.path.append("../..")
from db.utils.loading import import_csv_to_database
from db.DaoImpl.daoImpl_S import *
from db.DaoImpl.daoImpl_Y import *
from db.DaoImpl.daoImpl_X import *
from db.utils.Factor import *
from datetime import datetime
class Admin(base_dao):
    def __init__(self):
        factor=DaoFactory
        self.plants=factor.get_dao("Plants")
        self.familys=factor.get_dao("Plant_Family")
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
                import_csv_to_database("PlantFamily.csv", plant_Family_dao_Impl(), Plants)
                import_csv_to_database("PlantGenus.csv", plant_Genus_dao_Impl(), Plants)
                import_csv_to_database("PlantSpecies.csv", plant_Species_dao_Impl(), Plants)
                import_csv_to_database("PlantZone.csv", plant_Zone_dao_Impl(), Plants)
            elif(i=="3"):
                import_csv_to_database("careWorker.csv",careWorker_dao_Impl(), CareWorker)
                import_csv_to_database("careJob.csv",careJob_dao_Impl(), CareJob)
            elif(i=="4"):
                import_csv_to_database("pestInfo.csv",PestInfoDaoImpl(),PestInfo)
                import_csv_to_database("prevent.csv",PreventDaoImpl(),Prevent)
                import_csv_to_database("usage.csv",UsageDaoImpl(),Usage)
                import_csv_to_database("medicines.csv",MedicinesDaoImpl(),Medicines)
            elif(i=="5"):
                import_csv_to_database("Monitoring_Equipment.csv",Monitoring_Equipment_dao_Impl(), Monitoring_Equipment)
                import_csv_to_database("Monitoring_Personnel.csv",Monitoring_Personnel_dao_Impl(), Monitoring_Personnel)
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
            print('10.结束')
            i=input('所执行业务ID:')
            if(i=="1"):
                self.viewPlant(input('植物ID:'))
            elif(i=="2"):
                self.viewAllPlants()
            elif(i=="3"):
                self.viewSort(input('植物ID:'))
            elif(i=="4"):
                plant=Plants(input('植物ID:'),input('植物名:'),input('别名:'),input('形态特征:'),input('栽培技术要点:'),input('应用价值:'),input('植物介绍:'),input('创建人员:'),input('科ID:'),input('属ID:'),input('种ID:'),input('区域ID:'),datetime.now(),datetime.now())
                self.plant.update(plant)
            elif(i=="5"):
                family=PlantFamily(input('科ID:'),input('科名:'),input('科描述:'))
                self.family.update(family)
            elif(i=="6"):
                genus=PlantGenus(input('种ID:'),input('种名:'),input('种描述:'))
                self.genus.update(genus)
            elif(i=="7"):
                species=PlantSpecies(input('属ID:'),input('属名:'),input('属描述:'))
                self.species.update(species)
            elif(i=="8"):
                zone=PlantZone(input('区域id:'),input('省：'),input('市：'),input('县/乡：'),datetime.now(),datetime.now())
                self.zone.update(zone)
            elif(i=="9"):
                self.setConfigInfo()
            elif(i=="10"):
                break
            else:
                print('错误的执行ID')
    
