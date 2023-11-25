import GlobalVariables
from SegmentScreen.Segment import Segment
import re

segments = []
RECTANGLE_STARTING_Y = 300
RECTANGLE_WIDTH = GlobalVariables.SCREEN_WIDTH/(GlobalVariables.NUMBER_OF_SEGMENTS+1)
RECTANGLE_ENDING_Y = GlobalVariables.SCREEN_HEIGHT - 20
RECTANGLE_SPACING = RECTANGLE_WIDTH/(GlobalVariables.NUMBER_OF_SEGMENTS+1)
CIRCLE_STARTING_Y = RECTANGLE_STARTING_Y + 200
VOLTAGE_CIRCLE_SPACING = (RECTANGLE_ENDING_Y - CIRCLE_STARTING_Y)/GlobalVariables.VOLTAGE_SENSORS_PER_SEGMENT
TEXT_STARTING_Y = CIRCLE_STARTING_Y + 5
TEMP_CIRCLE_SPACING = (RECTANGLE_ENDING_Y - CIRCLE_STARTING_Y)/GlobalVariables.TEMP_SENSORS_PER_SEGMENT

class DisplaySegments():
    def __init__(self, app):
        self.app = app
        self.cv = app.cv
        self.stopFlag = True
        self.draw_segments()
        self.draw_voltage_status_circles()
        self.add_voltage_text_fields()
        self.draw_temp_status_circles()
        self.add_temp_text_fields()
        self.add_min_max_total_status_fields()
        self.add_min_max_total_text_fields()
        
    #Dynamically draw the five rectangles for the five segments
    def draw_segments(self):
        rectangleStartingX = RECTANGLE_SPACING
        rectangleEndingX = rectangleStartingX + RECTANGLE_WIDTH

        for i in range(0, GlobalVariables.NUMBER_OF_SEGMENTS):
            segments.append(Segment(self.cv.create_rectangle(rectangleStartingX, RECTANGLE_STARTING_Y, rectangleEndingX,
                    RECTANGLE_ENDING_Y, fill="#d0f4f9")))
            
            rectangleStartingX = rectangleEndingX + RECTANGLE_SPACING
            rectangleEndingX = rectangleStartingX + RECTANGLE_WIDTH

    # Draw the circles next to the voltages of each segment
    def draw_voltage_status_circles(self):
        starting_point_y = CIRCLE_STARTING_Y
        starting_point_x = RECTANGLE_SPACING + 10
        for i in range(0, GlobalVariables.NUMBER_OF_SEGMENTS):
            for j in range(0, GlobalVariables.VOLTAGE_SENSORS_PER_SEGMENT):
                segments[i].addVoltageStatusCircles(self.cv.create_oval(starting_point_x, 
                                                        starting_point_y, starting_point_x + 10, starting_point_y + 10, fill="green"))
                
                starting_point_y = starting_point_y + VOLTAGE_CIRCLE_SPACING

            starting_point_y = CIRCLE_STARTING_Y
            starting_point_x = starting_point_x + RECTANGLE_SPACING + RECTANGLE_WIDTH

    # Create the voltage text fields
    def add_voltage_text_fields(self):
        starting_point_y = TEXT_STARTING_Y
        starting_point_x = RECTANGLE_SPACING + 70
        for i in range(0, GlobalVariables.NUMBER_OF_SEGMENTS):
            for j in range(0, GlobalVariables.VOLTAGE_SENSORS_PER_SEGMENT):
                formattedText = "{:02}".format(j+1) + ": " + "UNK"
                segments[i].addVoltageTextFields(self.cv.create_text(starting_point_x, 
                                                        starting_point_y, text=formattedText, fill="black", font="Arial 10 bold"))
                
                starting_point_y = starting_point_y + VOLTAGE_CIRCLE_SPACING

            starting_point_y = TEXT_STARTING_Y
            starting_point_x = starting_point_x + RECTANGLE_SPACING + RECTANGLE_WIDTH

    # Create the temp status fields
    def draw_temp_status_circles(self):
        starting_point_y = CIRCLE_STARTING_Y
        starting_point_x = RECTANGLE_SPACING + RECTANGLE_WIDTH - 120
        for i in range(0, GlobalVariables.NUMBER_OF_SEGMENTS):
            for j in range(0, GlobalVariables.TEMP_SENSORS_PER_SEGMENT):
                segments[i].addTempStatusCircles(self.cv.create_oval(starting_point_x, 
                                                        starting_point_y, starting_point_x + 10, starting_point_y + 10, fill="green"))
                
                starting_point_y = starting_point_y + TEMP_CIRCLE_SPACING

            starting_point_y = CIRCLE_STARTING_Y
            starting_point_x = starting_point_x + RECTANGLE_SPACING + RECTANGLE_WIDTH

    # Create the temperature text fields
    def add_temp_text_fields(self):
        starting_point_y = TEXT_STARTING_Y
        starting_point_x = RECTANGLE_SPACING + RECTANGLE_WIDTH - 55
        for i in range(0, GlobalVariables.NUMBER_OF_SEGMENTS):
            for j in range(0, GlobalVariables.TEMP_SENSORS_PER_SEGMENT):
                formattedText = "{:02}".format(j+1) + ": " + str(678) + "F" #TODO: Remove Eventually
                segments[i].addVoltageTextFields(self.cv.create_text(starting_point_x, 
                                                        starting_point_y, text=formattedText, fill="black", font="Arial 10 bold"))
                
                starting_point_y = starting_point_y + TEMP_CIRCLE_SPACING

            starting_point_y = TEXT_STARTING_Y
            starting_point_x = starting_point_x + RECTANGLE_SPACING + RECTANGLE_WIDTH

    def add_min_max_total_text_fields(self):
        starting_point_y = RECTANGLE_STARTING_Y + 20
        starting_point_x = RECTANGLE_SPACING + 85

        for i in range(GlobalVariables.NUMBER_OF_SEGMENTS):
            
            segments[i].setMinId(self.cv.create_text((starting_point_x - 5), 
                                                        starting_point_y, text="MIN: UNK", fill="black", font="Arial 10 bold"))
            
            starting_point_y = starting_point_y + 30

            segments[i].setMaxId(self.cv.create_text(starting_point_x, 
                                                        starting_point_y, text="MAX: UNK", fill="black", font="Arial 10 bold"))
            
            starting_point_y = starting_point_y + 30
            
            segments[i].setAvgId(self.cv.create_text(starting_point_x, 
                                                        starting_point_y, text="AVG: UNK", fill="black", font="Arial 10 bold"))
            
            starting_point_y = RECTANGLE_STARTING_Y + 20
            starting_point_x = starting_point_x + RECTANGLE_SPACING + RECTANGLE_WIDTH


    def add_min_max_total_status_fields(self):
        starting_point_y = RECTANGLE_STARTING_Y + 13
        starting_point_x = RECTANGLE_SPACING + 10
        for i in range(GlobalVariables.NUMBER_OF_SEGMENTS):
            segments[i].setMinStatusId(self.cv.create_oval(starting_point_x, 
                                                starting_point_y, starting_point_x + 15, starting_point_y + 15, fill="green"))
            
            starting_point_y = starting_point_y + 30

            segments[i].setMaxStatusId(self.cv.create_oval(starting_point_x, 
                                                starting_point_y, starting_point_x + 15, starting_point_y + 15, fill="red"))
            
            starting_point_y = starting_point_y + 30
            
            segments[i].setAvgStatusId(self.cv.create_oval(starting_point_x, 
                                                starting_point_y, starting_point_x + 15, starting_point_y + 15, fill="gold"))
            
            starting_point_y = RECTANGLE_STARTING_Y + 13
            starting_point_x = starting_point_x + RECTANGLE_SPACING + RECTANGLE_WIDTH
    
    def updateVoltageData(self, data):
        vals = re.findall(r'(\d+(?:\.\d+)?)', data)
        segment = segments[int(vals[0]) - 1]
        busbar = int(vals[1]) - 1
        volt = float(vals[2])

        self.cv.itemconfig(segment.getVoltageTextFields()[busbar], text="{num:02}: {voltage:.2f} V".format(num = busbar+1, voltage = volt))
        segment.updateVoltageSensorReading(busbar, volt)

        self.changeStatusColor(GlobalVariables.MIN_ACCEPTABLE_VOLTAGE, GlobalVariables.MAX_ACCEPTABLE_VOLTAGE, 
                               GlobalVariables.WARNING_VOLTAGE_PLUS_MINUS, volt, segment.getVoltageStatusCircles()[busbar])

        avg = segment.getAverage()
        min = segment.getMin()
        max = segment.getMax()

        self.cv.itemconfig(segment.getMinId(), text="MIN: {minVolt:.2f} V".format(minVolt = min))
        self.changeStatusColor(GlobalVariables.MIN_ACCEPTABLE_VOLTAGE, GlobalVariables.MAX_ACCEPTABLE_VOLTAGE, 
                               GlobalVariables.WARNING_VOLTAGE_PLUS_MINUS, min, segment.getMinStatusId())
        
        self.cv.itemconfig(segment.getMaxId(), text="MAX: {maxVolt:.2f} V".format(maxVolt = max))
        self.changeStatusColor(GlobalVariables.MIN_ACCEPTABLE_VOLTAGE, GlobalVariables.MAX_ACCEPTABLE_VOLTAGE, 
                               GlobalVariables.WARNING_VOLTAGE_PLUS_MINUS, max, segment.getMaxStatusId())
        
        self.cv.itemconfig(segment.getAvgId(), text="AVG: {avgVolt:.2f} V".format(avgVolt = avg))
        self.changeStatusColor(GlobalVariables.MIN_ACCEPTABLE_VOLTAGE, GlobalVariables.MAX_ACCEPTABLE_VOLTAGE, 
                        GlobalVariables.WARNING_VOLTAGE_PLUS_MINUS, avg, segment.getAvgStatusId())


    def changeStatusColor(self, minVal, maxVal, yellowRange, currentVal, statusId):
        statusColor = "green"
        if (currentVal <= minVal or currentVal >= maxVal):
            statusColor = "red"
        elif (currentVal <= (minVal + yellowRange) or currentVal >= (maxVal - yellowRange)):
            statusColor = "gold"

        self.cv.itemconfig(statusId, fill=statusColor)