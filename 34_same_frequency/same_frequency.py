def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    return num_frequency(str(num1)) == num_frequency(str(num2))

def num_frequency (num): 
    counter = {}

    for n in num:
        counter[n] = counter.get(n, 0) + 1

    return counter


print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))