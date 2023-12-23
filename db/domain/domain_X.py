class Monitor:
    def __init__(self, diseaseID, name, create_time, update_time):
        self.diseaseID = diseaseID
        self.name = name
        self.create_time = create_time
        self.update_time = update_time

class Monitoring_Equipment:
    def __init__(self, id, time, place, object):
        self.id = id
        self.time = time
        self.place = place
        self.object = object
        
class Monitoring_Personnel:
    def __init__(self, id, name, sex, create_time, update_time, birth,tel):
        self.id = id
        self.name = name
        self.sex = sex
        self.create_time = create_time
        self.update_time = update_time
        self.birth = birth
        self.tel = tel