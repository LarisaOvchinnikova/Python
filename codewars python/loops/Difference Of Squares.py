# https://www.codewars.com/kata/558f9f51e85b46e9fa000025/train/python
def difference_of_squares(num):
    return sum([n for n in list(range(1, num+1))])**2 - sum([n**2 for n in list(range(1, num+1))])