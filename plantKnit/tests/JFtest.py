import sys
sys.path.append("../..")
from datetime import datetime
from plantKnit.user.管理员 import *

from db.utils.dao import *
from db.domain.domain_Y import *
from db.DaoImpl.daoImpl_Y import *
a=IllustrationDaoImpl()
IllustrationID="001"
IllustrationDescription="good"
IllustrationName="ins_1"
node=Illustration(IllustrationID,IllustrationDescription,IllustrationName)
a.insert(node)
temp=a.select("001")
temp.output()

newnode=Illustration("001","bad","ins_2")
a.update(newnode)
temp=a.select("001")
temp.output()

a.delete("001")
temp=a.select("001")


user=管理员()
family=plant_Family_dao_Impl()
genus=plant_Genus_dao_Impl()
species=plant_Species_dao_Impl()
zone=plant_Zone_dao_Impl()
plant=PlantsDaoImpl()
# line1=PlantFamily(1,"A科","god")
# line2=PlantGenus(1,"A属","good")
# line3=PlantSpecies(1,"A种","goood")
# line4=PlantZone(1,"A省","A市","A国",datetime.now(),datetime.now())
# line5=Plants(1,"A树","a树","bad","baad","baaaad","baaaaad","小a",1,1,1,1,datetime.now(),datetime.now())
# family.insert(line1)
# genus.insert(line2)
# species.insert(line3)
# zone.insert(line4)
#plant.insert(line5)
user.查看植物信息(1)
user.查看所有植物信息()
user.查看植物分类信息(1)