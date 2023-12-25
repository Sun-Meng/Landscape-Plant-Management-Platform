import sys
sys.path.append("../..")
from db.DaoImpl.daoImpl_S import *
from db.DaoImpl.daoImpl_Y import *
from db.DaoImpl.daoImpl_X import *
from db.utils.Factor import *
class Higher(object):
    def __init__(self):
        factory=DaoFactory()
        self.Higher=factory.get_Dao("Higher")
        