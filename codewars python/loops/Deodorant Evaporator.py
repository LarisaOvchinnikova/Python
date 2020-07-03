https://www.codewars.com/kata/523b4ff7adca849afe000035/train/python

def evaporator(content, evap_per_day, threshold):
    n = 0
    limit = content * threshold/100
    while content > limit:
        content = content - content * evap_per_day/100
        n += 1
    return n