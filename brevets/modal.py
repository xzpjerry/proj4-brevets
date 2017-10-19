# Conforming with MVC design
# Data_structure for a controle

from os import path
import re


class controle:

    def __init__(self, minSpeed=-1, maxSpeed=-1):
        self.minSpeed = minSpeed
        self.maxSpeed = maxSpeed

    def __str__(self):
        return str(self.minSpeed) + str(self.maxSpeed)


class controle_list():

    def __init__(self, controleList : str):
        self.controle_table = {}
        re_rule = re.compile(
            r'^([0-9]*)\-[0-9]*.*[mM]in\:([0-9\.]*).*[mM]ax\:([0-9\.]*)$')
        if path.isfile(controleList):
            with open(controleList, 'r') as f:
                for line in f.readlines():
                    tmp_match_result = re_rule.match(line)
                    if tmp_match_result:
                        self.controle_table[float(tmp_match_result.group(1))] = controle(
                            float(tmp_match_result.group(2)), float(tmp_match_result.group(3)))

        else:
            self.controle_table = {
                1000: controle(13.333, 26),
                600: controle(11.428, 28),
                400: controle(15, 30),
                200: controle(15, 32),
                0: controle(15, 34)
            }


class time_needed:
    __hours = None
    __mins = None

    @property
    def hours(self):    # for symmetrical purpose
        return self.__hours

    @property
    def mins(self):
        return round(self.__mins, 0)  # comply with ACP rules

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
