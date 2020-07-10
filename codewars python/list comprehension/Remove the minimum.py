https://www.codewars.com/kata/563cf89eb4747c5fb100001b/python
def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    else:
        m = min(numbers)
        return [el for i, el in enumerate(numbers) if i != numbers.index(m)]