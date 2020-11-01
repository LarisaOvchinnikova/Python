https://www.codewars.com/kata/525c65e51bf619685c000059
def cakes(recipe, available):
    arr = []
    for key in recipe:
        if key in available:
            arr.append(available[key]//recipe[key])
        else:
            return 0
    return min(arr)