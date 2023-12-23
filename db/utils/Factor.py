import sys

sys.path.append("../..")
from db.DaoImpl.daoImpl_Y import *
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
        else:
            return None