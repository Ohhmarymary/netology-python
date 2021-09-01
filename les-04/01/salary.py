def calculate(work_time, rate_time, prize):
    try:
        return (work_time*rate_time)+prize
    except TypeError:
        return
    