import sys
sys.path.append("../..")
from db.DaoImpl.daoImpl_S import *
from db.DaoImpl.daoImpl_Y import *
from db.DaoImpl.daoImpl_X import *
from db.utils.Factor import *
class 管理员(object):
    def __init__(self):
        factor=DaoFactory
        self.plants=factor.get_dao("Plants")
        factor.get_dao("")
        factor.get_dao("")
    def 查看植物信息(self,id):
        temp=self.plants.select(id)
        if(temp!=''):
            print(vars(temp))
        else:print("id有误")
    def 查看所有植物信息(self):
        temp=self.plants.select_all()
        for i in temp:
            print(vars(i))



