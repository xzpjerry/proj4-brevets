# Conforming with MVC design


class controle:

    def __init__(self, minSpeed=-1, maxSpeed=-1):
        self.minSpeed = minSpeed
        self.maxSpeed = maxSpeed

    def __str__(self):
        return str(self.minSpeed) + str(self.maxSpeed)


class time_needed:

    def __init__(self, hours=0, mins=0):
        self.hours = hours
        self.mins = mins
        #self._stdlize()

    def _stdlize(self):
        self.hours += (self.mins // 60)
        self.mins -= ((self.mins // 60) * 60)

    def combination(self, another_time_needed):
        assert type(another_time_needed) == type(self)
        self.hours += another_time_needed.hours
        self.mins += another_time_needed.mins
        self._stdlize()

    def __str__(self):
    	return "Hour: " + str(self.hours) + ", mins: " + str(self.mins)


controle_table = {
    600: controle(11.428, 28),
    400: controle(15, 30),
    200: controle(15, 32),
    0: controle(15, 34)
}
