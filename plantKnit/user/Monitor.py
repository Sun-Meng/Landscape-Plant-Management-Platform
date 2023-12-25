import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("../..")
from db.DaoImpl.daoImpl_S import *
from db.DaoImpl.daoImpl_Y import *
from db.DaoImpl.daoImpl_X import *
from db.utils.Factor import *
class Monitor(object):
    def __init__(self):
        factory=DaoFactory()
        self.Monitor=factory.get_Dao("Monitor")
        