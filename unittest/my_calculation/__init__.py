def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total
def mul(arg):
    total = 1
    for val in arg:
        if val==0:
            return 0
        else:
            total = total*val
    return total
        
