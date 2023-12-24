import sys
sys.path.append("../..")
from db.DaoImpl.daoImpl_S import *
from db.DaoImpl.daoImpl_Y import *
from db.DaoImpl.daoImpl_X import *
from db.utils.Factor import *
class 管理员(base_dao):
    def __init__(self):
        factor=DaoFactory
        self.plants=factor.get_dao("Plants")
        factor.get_dao("")
        factor.get_dao("")
        self.connection = self.get_conn() 
    def 查看植物信息(self,id):
        temp=self.plants.select(id)
        if(temp!=None):
            print(vars(temp))
        else:print("id有误")
    def 查看所有植物信息(self):
        temp=self.plants.selectAll()
        for i in temp:
            print(i)
    def 查看植物分类信息(self,id):
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


