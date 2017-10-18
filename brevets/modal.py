# Conforming with MVC design
# Data_structure for a controle

class controle:

    def __init__(self, minSpeed=-1, maxSpeed=-1):
        self.minSpeed = minSpeed
        self.maxSpeed = maxSpeed

    def __str__(self):
        return str(self.minSpeed) + str(self.maxSpeed)


class time_needed:
    __hours = None
    __mins = None

    @property
    def hours(self):
        return self.__hours

    @property
    def mins(self):
        return round(self.__mins, 0) # comply with ACP rules

    @hours.setter
    def hours(self, value):
        self.__hours = value

    @mins.setter
    def mins(self, value):
        self.__mins = value
        self._stdlize()

    def __init__(self, hours=0, mins=0):
        self.hours = hours
        self.mins = mins

    def _stdlize(self):
        self.__hours += (self.__mins // 60)
        self.__mins -= ((self.__mins // 60) * 60)

    def __str__(self):
    	return "Hour: " + str(self.hours) + ", mins: " + str(self.mins)


controle_table = {
    1000: controle(13.333, 26),
    600: controle(11.428, 28),
    400: controle(15, 30),
    200: controle(15, 32),
    0: controle(15, 34)
}
