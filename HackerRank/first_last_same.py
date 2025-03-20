###Check if the first and last numbers of a list are the same


def first_last_same(checklist):
    """ -step 1: make a list
    step 2: mention first number of the list
    step 3: mention last number of the list
    step 4: if first number == last number
    step 5: check the result"""
    first_num = checklist[0]
    last_num = checklist[-1]
    
    if first_num == last_num:
        return True
    else:
        return False
        
numbers_x = [10, 11, 12, 13, 10]
print(first_last_same(numbers_x))


numbers_y = [20, 30, 21, 33, 40]
print(first_last_same(numbers_y))