def solution(number):
    return sum([el for el in range(number) if el % 3 == 0 or el % 5 == 0])