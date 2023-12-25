class Monitor(object):
    def __init__(self, resultID, name, create_time, update_time):
        self.resultID = resultID
        self.name = name
        self.create_time = create_time
        self.update_time = update_time
        
    def get_resultID(self):
        return self.resultID
    
    def get_name(self):
        return self.name
    
    def get_create_time(self):
        return self.create_time
    
    def get_update_time(self):
        return self.update_time

class Monitoring_Equipment(object):
    def __init__(self, equipmentID, time, place, object):
        self.equipmentID = equipmentID
        self.time = time
        self.place = place
        self.object = object
        
    def get_equipmentID(self):
        return self.equipmentID
    
    def get_time(self):
        return self.time
    
    def get_place(self):
        return self.place
    
    def get_object(self):
        return self.object
        
class Monitoring_Personnel(object):
    def __init__(self, personID, name, sex, birth, tel, create_time, update_time):
        self.personID = str(personID)
        self.name = str(name)
        self.sex = str(sex)
        self.birth = str(birth)
        self.tel = str(tel)
        self.create_time = str(create_time)
        self.update_time = str(update_time)

    
    def get_personID(self):
        return self.personID
    
    def get_name(self):
        return self.name
    
    def get_sex(self):
        return self.sex
    
    def get_create_time(self):
        return self.create_time
    
    def get_update_time(self):
        return self.update_time
    
    def get_birth(self):
        return self.birth
    
    def get_tel(self):
        return self.tel