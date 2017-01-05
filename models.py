from app import  db
class iotDevice(db.Model):
    __tablename__ = 'iotDevice'
    __bind_key__ = 'mySql1'
    userName = db.Column (db.String(100))
    deviceNum = db.Column (db.String(40),  primary_key=True)
    def __init__(self, uName, deviceNum):
        self.userName = uName
        self.deviceNum = deviceNum

class iotDeviceBackup(db.Model):
    __tablename__ = 'iotDeviceBakup'
    __bind_key__ = 'mySql2'
    userName = db.Column (db.String(100))
    deviceNum = db.Column (db.String(40),  primary_key=True)
    def __init__(self, uName, deviceNum):
        self.userName = uName
        self.deviceNum = deviceNum

class iotLog(db.Model):
    __tablename__ = 'iotLog'
    __bind_key__ = 'mySql1'
    deviceNum = db.Column (db.String(40), primary_key=True)
    logData = db.Column (db.String(80))
    
    def __init__(self, logId, deviceNum, logData):
        self.deviceNum = deviceNum
        self.logData = logData

