import sys

sys.path.append("../..")
from db.daoImpl import *
class DaoFactory:
    def get_dao(dao_type):
        if dao_type=='User':
            return user_dao_Impl()
        elif dao_type == 'Illustration':
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
        elif dao_type =='Plant_Family':
            return plant_Family_dao_Impl()
        elif dao_type =='Plant_Genus':
            return plant_Genus_dao_Impl()
        elif dao_type =='Plant_Species':
            return plant_Species_dao_Impl()
        elif dao_type =='Plant_Zone':
            return plant_Zone_dao_Impl()
        elif dao_type == 'Shooting':
            return ShootingDaoImpl()
        elif dao_type == 'CareJob':
            return careJob_dao_Impl()
        elif dao_type == 'CareWorker':
            return careWorker_dao_Impl()
        elif dao_type == 'Monitor':
            return Monitor_dao_Impl()
        elif dao_type == 'Monitoring_Equipment':
            return Monitoring_Equipment_dao_Impl()
        elif dao_type == 'Monitoring_Personnel':
            return Monitoring_Personnel_dao_Impl() 
        else:
            return None