import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("..")
from db.DaoImpl.daoImpl_S import *
from db.DaoImpl.daoImpl_Y import *
from db.DaoImpl.daoImpl_X import *
from db.utils.Factor import *
from plantKnit.user.Admin import *
from plantKnit.user.Higher import *
from plantKnit.user.Monitor import *
from plantKnit.user.PlantCarer import * 
from datetime import datetime

def login(id,pwd):
    pass
#在这里实现获取用户类---工厂模式
#根据（id,pwd)去匹配类型
#生成对应的类（只有养护人员PlantCarer实例化 需要id)
    #需要
    #假如是管理员Admin
    #return Admin()
    #return 用户类class()


print('欢迎来到植物管理平台')
while(True):
    print('请登录')    
    user=login(input('ID:'),input('password:'))
    user.menu() #每个用户都有自己的子菜单 
    print('～～主页面～～')
    print('1.登录其它用户')
    print('2.退出系统')
    i=input('执行ID')
    if(i==1):continue
    elif(i==2):break
    else:print('错误执行ID')