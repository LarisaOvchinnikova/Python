https://www.codewars.com/kata/57cc981a58da9e302a000214
def small_enough(array, limit):
    return len([el for el in array if el <= limit ]) == len(array)