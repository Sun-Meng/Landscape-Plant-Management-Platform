#基础的增删改查已有，可在pass后增加自己的操作
class base:
    def insert(self, obj) -> bool:
        pass

    def delete(self, key) -> bool:
        pass

    def update(self, obj) -> bool:
        pass

    def select(self, key):
        pass

class IllustrationDao(base):
    pass
class UsageDao(base):
    pass

class MedicinesDao(base):
    pass

class PreventDao(base):
    pass

class PestInfoDao(base):
    pass

class PlantsDao(base):
    pass
        
class ShootingDao(base):
    pass
