"""
Open and close time calculations for ACP-sanctioned
brevets following rules described at
https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

# Global tables
# Distance (beyond which the speed requirements are:), min speed, max speed
rates = [(1000, 13.333, 26),
         (600, 11.428, 28),
         (400, 15, 30),
         (200, 15, 32),
         (0, 15, 34)]

# The prescribed finishing times, in hours:
finish_times = {200: 13.5,
                300: 20,
                400: 27,
                600: 40,
                1000: 75}


def get_dt(control_dist_km, type):
    """
    Function to calculate the opening or closing time for a brevit controle.
        Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
       type:
           An int variable to specify closing or opening time,
           Type one is for closing times, type two is for opening times.
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    remaining = control_dist_km
    dt = 0
    for i in rates:
        # Check how far we are going to travel at the current rate.
        dist_at_cur_rate = remaining - i[0]
        if dist_at_cur_rate < 0:
            continue
        else:
            # Add the appropriate amount of time, decrement remaining distance.
            dt += dist_at_cur_rate / i[type]
            remaining -= dist_at_cur_rate
    return dt


def dt_to_arrow(dt, start_time):
    """
    Add a delta time (in hours) to a start time.
        Args:
      dt: a float number of hours to add to start_time.
      start_time: an arrow object.
    return: an arrow time object in iso format.
    """
    # Convert to minutes and round to nearest minute:
    mins = int((dt * 60) + .5)
    return arrow.get(start_time).shift(minutes=+mins).isoformat()


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
    # Check special condition of a controle point past brevit distance:
    if control_dist_km > brevet_dist_km:
        control_dist_km = brevet_dist_km
    # Calc open time. The two means we want open time:
    dt = get_dt(control_dist_km, 2)
    # Convert time to an arrow object and return it:
    return dt_to_arrow(dt, brevet_start_time)


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
    # Check special cases of zero and greater than max distance.
    if control_dist_km >= brevet_dist_km:
        dt = finish_times[brevet_dist_km]
    elif control_dist_km == 0:
        dt = 1
    else:
        # Calc close time. The one means we want close time:
        dt = get_dt(control_dist_km, 1)
    # Convert time to an arrow object and return it:
    return dt_to_arrow(dt, brevet_start_time)
