def narcissistic( value ):
    sum = 0;
    value = str(value)
    digits = len(value)
    for i in value:
        sum = sum + int(i)**digits;
    if sum == int(value):
        return True
    else:
        return False