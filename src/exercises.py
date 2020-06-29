def reverse_list(input_list):
    """
    Reverses order of elements in list input_list.
    """
    return input_list[::-1]


def count_digits(number):
    """
    Return count of digits
    """
    n = int(number)
    count = 0
    
    while n!=0:
        count += 1
        n = int(n/10)
       
    return count