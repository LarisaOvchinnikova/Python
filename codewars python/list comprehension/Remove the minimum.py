def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    else:
        m = min(numbers)
        return [el for i, el in enumerate(numbers) if i != numbers.index(m)]