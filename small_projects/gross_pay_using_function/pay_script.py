def new_funct(work_hour, rate):
    min_hour = 40

    if work_hour <= min_hour:
        pay = work_hour * rate
    elif work_hour > min_hour:
        work_hour_ot = work_hour - min_hour
        pay_ot = (work_hour_ot * 1.5) * rate
        pay = (min_hour * rate) + pay_ot
    return pay
