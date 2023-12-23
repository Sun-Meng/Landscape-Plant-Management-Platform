class Monitor(object):
    def __init__(self, diseaseID, name, create_time, update_time):
        self.diseaseID = diseaseID
        self.name = name
        self.create_time = create_time
        self.update_time = update_time
        
    def get_diseaseID(self):
        return self.diseaseID
    
    def get_name(self):
        return self.name
    
    def get_create_time(self):
        return self.create_time
    
    def get_update_time(self):
        return self.update_time

class Monitoring_Equipment(object):
    def __init__(self, id, time, place, object):
        self.id = id
        self.time = time
        self.place = place
        self.object = object
        
    def get_id(self):
        return self.id
    
    def get_time(self):
        return self.time
    
    def get_place(self):
        return self.place
    
    def get_object(self):
        return self.object
        
class Monitoring_Personnel(object):
    def __init__(self, id, name, sex, create_time, update_time, birth,tel):
        self.id = id
        self.name = name
        self.sex = sex
        self.create_time = create_time
        self.update_time = update_time
        self.birth = birth
        self.tel = tel
    
    def get_id(self):
        return self.id
    
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