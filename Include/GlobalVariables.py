import pyautogui

#TODO: I want to eventually import from properties file to make it easier to change

NUMBER_OF_SEGMENTS = 5
VOLTAGE_SENSORS_PER_SEGMENT = 14
TEMP_SENSORS_PER_SEGMENT = 12
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

COM_PORT = "COM9"
BAUD_RATE = 115200

#Needs to be in segment - busbar - value order. The formatting can be anything
UART_FORMATS = {
    "SegmentDisplay.updateVoltageData" : "voltage s[0-9]{1,12}? b[0-9]{1,12}? (\d+(?:[\.\,]\d{1,12})?)$",
    "SegmentDisplay.updateTempData" : "temperature s[0-9]{1,12}? t[0-9]{1,12}? (\d+(?:[\.\,]\d{1,12})?)$"
}

INFO_SCREENS = {}

#VOLTAGE INFO
MAX_ACCEPTABLE_VOLTAGE = 4.2
MIN_ACCEPTABLE_VOLTAGE = 2.5
WARNING_VOLTAGE_PLUS_MINUS = 0.3


