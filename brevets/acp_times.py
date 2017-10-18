"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
from modal import controle_table, controle, time_needed  # data

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#


def open_close_time_router(control_dist_km, brevet_dist_km, brevet_start_time, ID):
  accumulator = time_needed()

  brevet_start_time = arrow.get(brevet_start_time)
  for km in controle_table:
    if km > brevet_dist_km or km > control_dist_km:
      continue  # skip higher km value

    this_part_dist = control_dist_km - km
    control_dist_km -= this_part_dist

    if ID == "OPEN":
      hour_needed = this_part_dist // controle_table[km].maxSpeed
      min_needed = (this_part_dist / controle_table[km].maxSpeed -
                    this_part_dist // controle_table[km].maxSpeed) * 60
    else:
      hour_needed = this_part_dist // controle_table[km].minSpeed
      min_needed = (this_part_dist / controle_table[km].minSpeed -
                    this_part_dist // controle_table[km].minSpeed) * 60 + 10

    min_needed = round(min_needed, 0)  # comply with ACP std

    this_part_time_needed = time_needed(hour_needed, min_needed)
    accumulator.combination(this_part_time_needed)

  result_time = brevet_start_time.shift(
      hours=accumulator.hours, minutes=accumulator.mins)

  print(accumulator)

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

  # <default> return arrow.now().isoformat()


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
