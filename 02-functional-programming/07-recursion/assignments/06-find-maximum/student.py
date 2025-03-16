def findMaximum(list):
    if len(list) == 0:
        raise IndexError
    elif len(list) == 1:
        return list[0]
    else:
        last = list[-1]
        other = findMaximum(list[:-1])
        return last if last > other else other