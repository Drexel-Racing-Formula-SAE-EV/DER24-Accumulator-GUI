import GlobalVariables

class Segment:
    def __init__(self, id):
        self.idNum = id
        self.voltageSensorsTextFields = []
        self.voltageSensorsStatusCircles = []
        self.voltageSensorReading = []
        self.tempSensorsTextField = []
        self.tempSensorsStatusCircles = []
        self.idNum = None
        self.minId = None
        self.maxId = None
        self.totalId = None

    def addVoltageSensorReading(self, voltage):
        self.voltageSensorReading.append(voltage)

    def getVoltageSensorReading(self):
        return self.voltageSensorReading

    def addVoltageTextFields(self, text):
        self.voltageSensorsTextFields.append(text)

    def getVoltageTextFields(self):
        return self.voltageSensorsTextFields

    def addVoltageStatusCircles(self, circle):
        self.voltageSensorsStatusCircles.append(circle)

    def getVoltageStatusCircles(self):
        return self.voltageSensorsStatusCircles

    def addTempSensors(self, temps):
        pass

    def addTempStatusCircles(self, temp):
        self.tempSensorsStatusCircles.append(temp)

    def getTempStatusCircles(self):
        return self.tempSensorsStatusCircles

    def addTempTextFields(self, text):
        self.tempSensorsTextField.append(text)

    def getTempTextFields(self):
        return self.tempSensorsTextField
    
    def getId(self):
        return self.idNum

    def getMin(self):
        pass

    def getMax(self):
        pass

    def getTotal(self):
        pass

    def setMinStatusId(self, id):
        self.minId = id

    def getMinStatusId(self):
        return self.minId
    
    def setMaxStatusId(self, id):
        self.maxId = id

    def setTotalId(self, id):
        self.totalId = id

    def getTotalId(self):
        return self.totalId

