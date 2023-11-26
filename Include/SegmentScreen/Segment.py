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

        self.tempSensorReading = { }
        for i in range(GlobalVariables.TEMP_SENSORS_PER_SEGMENT):
            self.tempSensorReading[i] = None

        self.tempSensorsTextField = []
        self.tempSensorsStatusCircles = []
        self.idNum = None
        self.minIdVoltage = None
        self.maxIdVoltage = None
        self.averageIdVoltage = None
        self.minStatusIdVoltage = None
        self.maxStatusIdVoltage = None
        self.averageStatusIdVoltage = None
        self.minIdTemp = None
        self.maxIdTemp = None
        self.averageIdTemp = None
        self.minStatusIdTemp = None
        self.maxStatusIdTemp = None
        self.averageStatusIdTemp = None

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

    def updateTempSensorReading(self, sensor, temp):
        self.tempSensorReading.update({sensor : temp})

    def getTempSensorReading(self):
        return self.tempSensorReading

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

    def getMinVoltage(self):
        min = float("inf")
        for i in range(0, GlobalVariables.VOLTAGE_SENSORS_PER_SEGMENT):
            if (self.getVoltageSensorReading()[i] != None and min >= self.getVoltageSensorReading()[i]):
                min = self.getVoltageSensorReading()[i]

        return min

    def getMaxVoltage(self):
        max = float("-inf")
        for i in range(0, GlobalVariables.VOLTAGE_SENSORS_PER_SEGMENT):
            if (self.getVoltageSensorReading()[i] != None and max <= self.getVoltageSensorReading()[i]):
                max = self.getVoltageSensorReading()[i]

        return max

    def getTotalVoltage(self):
        total = 0
        for i in range(0, GlobalVariables.VOLTAGE_SENSORS_PER_SEGMENT):
            if (self.getVoltageSensorReading()[i] != None):
                total += self.getVoltageSensorReading()[i]

        return total
    
    def getAverageVoltage(self):
        return self.getTotalVoltage()/GlobalVariables.VOLTAGE_SENSORS_PER_SEGMENT

    def setMinStatusIdVoltage(self, id):
        self.minStatusIdVoltage = id

    def getMinStatusIdVoltage(self):
        return self.minStatusIdVoltage
    
    def setMinIdVoltage(self, id):
        self.minIdVoltage = id

    def getMinIdVoltage(self):
        return self.minIdVoltage
    
    def setMaxStatusIdVoltage(self, id):
        self.maxStatusIdVoltage = id

    def getMaxStatusIdVoltage(self):
        return self.maxStatusIdVoltage

    def setMaxIdVoltage(self, id):
        self.maxIdVoltage = id

    def getMaxIdVoltage(self):
        return self.maxIdVoltage
    
    def setAvgStatusIdVoltage(self, id):
        self.averageStatusIdVoltage = id

    def getAvgStatusIdVoltage(self):
        return self.averageStatusIdVoltage

    def setAvgIdVoltage(self, id):
        self.averageIdVoltage = id

    def getAvgIdVoltage(self):
        return self.averageIdVoltage
    
    def getMinTemp(self):
        min = float("inf")
        for i in range(0, GlobalVariables.TEMP_SENSORS_PER_SEGMENT):
            if (self.getTempSensorReading()[i] != None and min >= self.getTempSensorReading()[i]):
                min = self.getTempSensorReading()[i]

        return min

    def getMaxTemp(self):
        max = float("-inf")
        for i in range(0, GlobalVariables.TEMP_SENSORS_PER_SEGMENT):
            if (self.getTempSensorReading()[i] != None and max <= self.getTempSensorReading()[i]):
                max = self.getTempSensorReading()[i]

        return max

    def getTotalTemp(self):
        total = 0
        for i in range(0, GlobalVariables.TEMP_SENSORS_PER_SEGMENT):
            if (self.getTempSensorReading()[i] != None):
                total += self.getTempSensorReading()[i]

        return total
    
    def getAverageTemp(self):
        return self.getTotalTemp()/GlobalVariables.TEMP_SENSORS_PER_SEGMENT

    def setMinStatusIdTemp(self, id):
        self.minStatusIdTemp = id

    def getMinStatusIdTemp(self):
        return self.minStatusIdTemp
    
    def setMinIdTemp(self, id):
        self.minIdTemp = id

    def getMinIdTemp(self):
        return self.minIdTemp
    
    def setMaxStatusIdTemp(self, id):
        self.maxStatusIdTemp = id

    def getMaxStatusIdTemp(self):
        return self.maxStatusIdTemp

    def setMaxIdTemp(self, id):
        self.maxIdTemp = id

    def getMaxIdTemp(self):
        return self.maxIdTemp
    
    def setAvgStatusIdTemp(self, id):
        self.averageStatusIdTemp = id

    def getAvgStatusIdTemp(self):
        return self.averageStatusIdTemp

    def setAvgIdTemp(self, id):
        self.averageIdTemp = id

    def getAvgIdTemp(self):
        return self.averageIdTemp

