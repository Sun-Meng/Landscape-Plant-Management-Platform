import sys
sys.path.append("../..")
from db.DaoImpl.daoImpl_S import *
from db.DaoImpl.daoImpl_Y import *
from db.DaoImpl.daoImpl_X import *
from db.utils.Factor import *
class Monitor(object):
    def __init__(self):
        factory=DaoFactory()
        self.Monitor=factory.getDao("Monitor")
        