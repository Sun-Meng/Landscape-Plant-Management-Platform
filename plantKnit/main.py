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
    factory=DaoFactory
    user=factory.get_dao("User")
    userId=input('ID:')
    password=input('password:')

    if user.login(userId, password):
        workertype = str(user.type(userId, password))
        print(workertype)
        if workertype.replace(" ","") =='养护人员':
            identity=PlantCarer(userId)
            print(f"养护人员{userId}登录成功！")
        elif workertype.replace(" ","") =='监测人员':
            identity=Monitor()
            print(f"监测人员{userId}登录成功！")
        elif workertype.replace(" ","") =='上层主管':
            identity=Higher()
            print(f"主管{userId}登录成功！")
        elif workertype.replace(" ","") =='系统管理员':
            identity=Admin()
            print(f"系统管理员{userId}登录成功！")
    else:
        print("登录失败，请检查用户名和密码。")
        print()
   
    identity.menu() #每个用户都有自己的子菜单 
    print('～～主页面～～')
    print('1.登录其它用户')
    print('2.退出系统')
    i=input('执行ID:') #这里得到的是str类型
    if(i=="1"):continue
    elif(i=="2"):
        print("您已退出系统")
        break
    else:
        print('错误执行ID')