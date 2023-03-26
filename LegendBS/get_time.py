def get_time(time: int):
    if time >= 86400:
        time = int(time / (60 * 60 * 24))
        unit = "days"
    ftime = f"{time} {unit}"
    elif time >= 3600 < 86400:
        time = int(time / (60 * 60))
        unit = "hours"
    ftime = f"{time} {unit}"
    elif time >= 60 < 3600:
        time = int(time / 60)
        unit = "minutes"
    ftime = f"{time} {unit}"
    return ftime
