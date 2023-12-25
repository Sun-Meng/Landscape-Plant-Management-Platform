import sys
sys.path.append("../..")
from db.DaoImpl.daoImpl_S import *
from db.DaoImpl.daoImpl_Y import *
from db.DaoImpl.daoImpl_X import *
from db.utils.Factor import *
from datetime import datetime
class Admin(base_dao):
    def __init__(self):
        factor=DaoFactory()
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
                updateSort(self,familyWHERE 
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
    def menu():
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
            print('9.结束')
            i=input('所执行业务ID：')
            if(i==1):
                viewPlant(input('植物ID'))
            elif(i==2):
                viewAllPlants()
            elif(i==3):
                viewSort(input('植物ID'))
            elif(i==4):
                plant=Plant(input('植物ID'),input('植物名'),input('忘了啥内容'),input('忘了啥内容'),input('忘了啥内容'),input('忘了啥内容'),input('忘了啥内容'),datetime.now(),datetime.now(),input('科ID'),input('属ID'),input('种ID'),input('区域ID'))
                self.plant.update(plant)
            elif(i==5):
                family=Plant_Family(input('科ID'),input('科名'),input('科描述'))
                self.family.update(family)
            elif(i==7):
                species=Plant_Species(input('属ID'),input('属名'),input('属描述'))
                self.species.update(species)
            elif(i==6):
                genus=Plant_Genus(input('种ID'),input('种名'),input('种描述'))
                self.genus.update(genus)
            elif(i==8):
                zone=Plant_Zone(input('区域id'),input('省'),input('国家'),input('市'),datetime.now(),datetime.now())
                self.zone.update(zone)
            elif(i==9):
                break
            else:
                print('错误的执行ID')
    
#子菜单：系统信息配置
#按业务进行配置
#  if name_type == '植物养护':
#     import_csv_to_database(csv_filename, dao_instance, entity_class)
#  elif name_type == '植物监测':
#     import_csv_to_database(csv_filename, dao_instance, entity_class)
#  elif name_type == '植物病虫害':
#     import_csv_to_database(csv_filename, dao_instance, entity_class)
