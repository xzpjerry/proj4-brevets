"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
from modal import *  # data

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#

def get_hour(this_part_dist, divisor_speed):
  return this_part_dist // divisor_speed

def get_min(this_part_dist, divisor_speed):
  return (this_part_dist / divisor_speed) % 1 * 60


def open_close_time_router(control_dist_km, brevet_dist_km, brevet_start_time, ID):
  hour_needed = 0
  min_needed = 0
  brevet_start_time = arrow.get(brevet_start_time)
  total_time_needed = time_needed()
  
  for km in controle_table:
    if km > brevet_dist_km or km > control_dist_km:
      continue  # skip higher km value
    if control_dist_km == 0:
      break

    this_part_dist = control_dist_km - km
    control_dist_km -= this_part_dist

    if ID == "OPEN":
      divisor_speed = controle_table[km].maxSpeed
    else:
      divisor_speed = controle_table[km].minSpeed

    hour_needed += get_hour(this_part_dist, divisor_speed)
    min_needed += get_min(this_part_dist, divisor_speed)
    print("hour_needed: ", hour_needed , " min_needed: ", min_needed)

  total_time_needed.hours = hour_needed
  total_time_needed.mins = min_needed

  result_time = brevet_start_time.shift(
      hours=total_time_needed.hours, minutes=total_time_needed.mins)
  print(total_time_needed)

  return result_time.isoformat()


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
  """
  Args:
     control_dist_km:  number, the control distance in kilometers
     brevet_dist_km: number, the nominal distance of the brevet
         in kilometers, which must be one of 200, 300, 400, 600,
         or 1000 (the only official ACP brevet distances)
     brevet_start_time:  An ISO 8601 format date-time string indicating
         the official start time of the brevet
  Returns:
     An ISO 8601 format date string indicating the control open time.
     This will be in the same time zone as the brevet start time.
  """
  return open_close_time_router(control_dist_km, brevet_dist_km, brevet_start_time, "OPEN")


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
  """
  Args:
     control_dist_km:  number, the control distance in kilometers
        brevet_dist_km: number, the nominal distance of the brevet
        in kilometers, which must be one of 200, 300, 400, 600, or 1000
        (the only official ACP brevet distances)
     brevet_start_time:  An ISO 8601 format date-time string indicating
         the official start time of the brevet
  Returns:
     An ISO 8601 format date string indicating the control close time.
     This will be in the same time zone as the brevet start time.
  """
  return open_close_time_router(control_dist_km, brevet_dist_km, brevet_start_time, "CLOSE")
