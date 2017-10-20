# Conforming with MVC design pattern
# Data_structure for a controle and overall time limit module

from os import path
import re


class time_needed:
    '''
    A silly way to comply with ACP's rules,
    to arrange hours and minutes.
    I would prefer to use arrow's shifting directly
    if we don't care the precision.
    '''
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


class controle:

    def __init__(self, minSpeed=0, maxSpeed=0):
        self.minSpeed = minSpeed
        self.maxSpeed = maxSpeed

    def __str__(self):
        return str(self.minSpeed) + str(self.maxSpeed)


class controle_overall_list():
    '''
    read controle_overall_limitList info from data/
    '''

    def __init__(self, controle_overall_limitList: str):
        self.overall_time_limit_table = {}
        controle_overall_limit_rule = re.compile(
            r'^([0-9]*).*[hH]ours\:([0-9]*).*[mM]ins\:([0-9]*)$')

        if path.isfile(controle_overall_limitList):
            with open(controle_overall_limitList, 'r') as f:
                for line in f.readlines():
                    tmp_match_result = controle_overall_limit_rule.match(line)
                    if tmp_match_result:
                        km = float(tmp_match_result.group(1))
                        hrs = float(tmp_match_result.group(2))
                        mins = float(tmp_match_result.group(3))
                        self.overall_time_limit_table[km] = time_needed(hrs, mins)


class controle_list():
    '''
    read controle spec from data/
    '''

    def __init__(self, controleList: str):
        self.controle_table = {}
        controle_speed_rule = re.compile(
            r'^([0-9]*)\-([0-9]*).*[mM]in\:([0-9\.]*).*[mM]ax\:([0-9\.]*)$')

        if path.isfile(controleList):
            with open(controleList, 'r') as f:
                for line in f.readlines():
                    tmp_match_result = controle_speed_rule.match(line)
                    if tmp_match_result:
                        min_km = float(tmp_match_result.group(1))
                        max_km = float(tmp_match_result.group(2))
                        minSpeed = float(tmp_match_result.group(3))
                        maxSpeed = float(tmp_match_result.group(4))

                        self.controle_table[min_km] = controle(
                            minSpeed, maxSpeed)