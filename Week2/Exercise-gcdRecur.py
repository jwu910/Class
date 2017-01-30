def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b,a%b)           
    
"""
a = b + (a%b)
b = c + (b%c)
c = d + (c%d)
function gcd(a, b)
    if b = 0
       return a; 
    else
       return gcd(b, a mod b);


"""

        
        
        
        
        
        
print(gcdRecur(25,5))