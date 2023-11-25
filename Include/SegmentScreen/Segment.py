import GlobalVariables
import sys

class Segment:
    def __init__(self, id):
        self.idNum = id
        self.voltageSensorsTextFields = []
        self.voltageSensorsStatusCircles = []
        self.voltageSensorReading = { }
        for i in range(GlobalVariables.VOLTAGE_SENSORS_PER_SEGMENT):
            self.voltageSensorReading[i] = None

        self.tempSensorsTextField = []
        self.tempSensorsStatusCircles = []
        self.idNum = None
        self.minId = None
        self.maxId = None
        self.averageId = None
        self.minStatusId = None
        self.maxStatusId = None
        self.averageStatusId = None

    def updateVoltageSensorReading(self, busbar, voltage):
        self.voltageSensorReading.update({busbar : voltage})

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
        min = float("inf")
        for i in range(0, GlobalVariables.VOLTAGE_SENSORS_PER_SEGMENT):
            if (self.getVoltageSensorReading()[i] != None and min >= self.getVoltageSensorReading()[i]):
                min = self.getVoltageSensorReading()[i]

        return min

    def getMax(self):
        max = float("-inf")
        for i in range(0, GlobalVariables.VOLTAGE_SENSORS_PER_SEGMENT):
            if (self.getVoltageSensorReading()[i] != None and max <= self.getVoltageSensorReading()[i]):
                max = self.getVoltageSensorReading()[i]

        return max

    def getTotal(self):
        total = 0
        for i in range(0, GlobalVariables.VOLTAGE_SENSORS_PER_SEGMENT):
            if (self.getVoltageSensorReading()[i] != None):
                total += self.getVoltageSensorReading()[i]

        return total
    
    def getAverage(self):
        return self.getTotal()/GlobalVariables.VOLTAGE_SENSORS_PER_SEGMENT

    def setMinStatusId(self, id):
        self.minStatusId = id

    def getMinStatusId(self):
        return self.minStatusId
    
    def setMinId(self, id):
        self.minId = id

    def getMinId(self):
        return self.minId
    
    def setMaxStatusId(self, id):
        self.maxStatusId = id

    def getMaxStatusId(self):
        return self.maxStatusId

    def setMaxId(self, id):
        self.maxId = id

    def getMaxId(self):
        return self.maxId
    
    def setAvgStatusId(self, id):
        self.averageStatusId = id

    def getAvgStatusId(self):
        return self.averageStatusId

    def setAvgId(self, id):
        self.averageId = id

    def getAvgId(self):
        return self.averageId

