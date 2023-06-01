def study_schedule(permanence_period, target_time):
    value = 0
    if target_time is None:
        return None
    for tuple in permanence_period:
        if not(isinstance(tuple[0], int)) or not(isinstance(tuple[1], int)):
           return None
        elif target_time >= tuple[0] and target_time <= tuple[1]:
            value += 1   
    return value
