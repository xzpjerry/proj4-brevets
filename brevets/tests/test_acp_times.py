from acp_times import *
import arrow

import nose
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

brevet_start_time = arrow.now()
brevet_start_time_iso = brevet_start_time.isoformat()

test_cases = {
    0: [(0, 0), (1, 0)],
    60: [(1, 46), (4, 0)],
    120: [(3, 32), (8, 0)],
    175: [(5, 9), (11, 40)],
    200: [(5, 53), (13, 20)],
    350: [(10, 34), (23, 20)],
    550: [(17, 8), (36, 40)],
    890: [(29, 9), (65, 23)],
    1000: [(33, 5), (75, 0)],
    1010: [(33, 5), (75, 0)]
}

test_cases2 = {
    0: [(0, 0), (1, 0)],
    60: [(1, 46), (4, 0)],
    120: [(3, 32), (8, 0)],
    175: [(5, 9), (11, 40)],
    200: [(5, 53), (13, 20)],
    350: [(10, 34), (23, 20)],
    550: [(17, 8), (36, 40)],
    600: [(18, 48), (40, 0)],
    610: [(18, 48), (40, 0)]
}

test_cases3 = {
    0: [(0, 0), (1, 0)],
    60: [(1, 46), (4, 0)],
    120: [(3, 32), (8, 0)],
    175: [(5, 9), (11, 40)],
    200: [(5, 53), (13, 20)],
    350: [(10, 34), (23, 20)],
    400: [(12, 8), (27, 0)],
    410: [(12, 8), (27, 0)]
}

test_cases4 = {
    0: [(0, 0), (1, 0)],
    60: [(1, 46), (4, 0)],
    120: [(3, 32), (8, 0)],
    175: [(5, 9), (11, 40)],
    200: [(5, 53), (13, 20)],
    300: [(9, 0), (20, 0)],
    350: [(9, 0), (20, 0)]
}

test_cases5 = {
    0: [(0, 0), (1, 0)],
    60: [(1, 46), (4, 0)],
    120: [(3, 32), (8, 0)],
    175: [(5, 9), (11, 40)],
    200: [(5, 53), (13, 30)],
    210: [(5, 53), (13, 30)]
}

def test_a_1000km_brevet():
    for case in test_cases:
        print(case)
        time_period = test_cases[case]
        my_acp_open_result = open_time(case, 1000, brevet_start_time_iso)
        official_open_result = brevet_start_time.shift(
            hours=time_period[0][0], minutes=time_period[0][1]).isoformat()
        my_acp_close_result = close_time(case, 1000, brevet_start_time_iso)
        official_close_result = brevet_start_time.shift(
            hours=time_period[1][0], minutes=time_period[1][1]).isoformat()

        assert my_acp_open_result == official_open_result
        assert my_acp_close_result == official_close_result

def test_a_600km_brevet():
    for case in test_cases2:
        print(case)
        time_period = test_cases2[case]
        my_acp_open_result = open_time(case, 600, brevet_start_time_iso)
        official_open_result = brevet_start_time.shift(
            hours=time_period[0][0], minutes=time_period[0][1]).isoformat()
        my_acp_close_result = close_time(case, 600, brevet_start_time_iso)
        official_close_result = brevet_start_time.shift(
            hours=time_period[1][0], minutes=time_period[1][1]).isoformat()
        assert my_acp_open_result == official_open_result
        assert my_acp_close_result == official_close_result

def test_a_400km_brevet():
    for case in test_cases3:
        print(case)
        time_period = test_cases3[case]
        my_acp_open_result = open_time(case, 400, brevet_start_time_iso)
        official_open_result = brevet_start_time.shift(
            hours=time_period[0][0], minutes=time_period[0][1]).isoformat()
        my_acp_close_result = close_time(case, 400, brevet_start_time_iso)
        official_close_result = brevet_start_time.shift(
            hours=time_period[1][0], minutes=time_period[1][1]).isoformat()
        assert my_acp_open_result == official_open_result
        assert my_acp_close_result == official_close_result

def test_a_300km_brevet():
    for case in test_cases4:
        print(case)
        time_period = test_cases4[case]
        my_acp_open_result = open_time(case, 300, brevet_start_time_iso)
        official_open_result = brevet_start_time.shift(
            hours=time_period[0][0], minutes=time_period[0][1]).isoformat()
        my_acp_close_result = close_time(case, 300, brevet_start_time_iso)
        official_close_result = brevet_start_time.shift(
            hours=time_period[1][0], minutes=time_period[1][1]).isoformat()
        print(my_acp_open_result, official_open_result)
        print(my_acp_close_result, official_close_result)
        assert my_acp_open_result == official_open_result
        assert my_acp_close_result == official_close_result

def test_a_200km_brevet():
    for case in test_cases5:
        print(case)
        time_period = test_cases5[case]
        my_acp_open_result = open_time(case, 200, brevet_start_time_iso)
        official_open_result = brevet_start_time.shift(
            hours=time_period[0][0], minutes=time_period[0][1]).isoformat()
        my_acp_close_result = close_time(case, 200, brevet_start_time_iso)
        official_close_result = brevet_start_time.shift(
            hours=time_period[1][0], minutes=time_period[1][1]).isoformat()
        assert my_acp_open_result == official_open_result
        assert my_acp_close_result == official_close_result
