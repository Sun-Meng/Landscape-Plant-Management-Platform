import sys

sys.path.append("../..")
from db.DaoImpl.daoImpl_S import *
from db.DaoImpl.daoImpl_Y import *
from db.DaoImpl.daoImpl_X import *
class DaoFactory:
    def get_dao(dao_type):
        if dao_type == 'Illustration':
            return IllustrationDaoImpl()
        elif dao_type == 'Usage':
            return UsageDaoImpl()
        elif dao_type == 'Medicines':
            return MedicinesDaoImpl()
        elif dao_type == 'Prevent':
            return PreventDaoImpl()
        elif dao_type == 'PestInfo':
            return PestInfoDaoImpl()
        elif dao_type == 'Plants':
            return PlantsDaoImpl()
        elif dao_type == 'Shooting':
            return ShootingDaoImpl()
        
        elif dao_type == 'CareJob':
            return careJob_dao_Impl()
        elif dao_type == 'Medicines':
            return Monitor_dao_Impl()
        elif dao_type == 'Prevent':
            return Monitoring_Equipment_dao_Impl()
        elif dao_type == 'PestInfo':
            return Monitoring_Personnel_dao_Impl() 
        else:
            return None