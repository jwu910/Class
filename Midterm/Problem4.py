# Midterm Problem 4
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''        
    exponent = 0

    while True:
        if abs(num-(base**exponent)) <= abs(num-(base**(exponent+1))):
            return exponent
        else:
            exponent += 1