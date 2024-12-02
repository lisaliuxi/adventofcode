import pandas as pd
import numpy as np 


def clean_nan_list(original_list):    
    cleaned_list = [x for x in original_list if x is not None and str(x) !='nan']
    return cleaned_list

def check_safe(row):
    
    list1 = clean_nan_list(row)  # rmv nan as report in diff length
    
    max_number_ind = list1.index(max(list1)) # get max number index

    if max_number_ind in [0, len(list1)-1]:  # check if max number at the first or last, if not, order def not correct
        
        reverse_order = sorted(list1, reverse=True)
        order = sorted(list1)

        if reverse_order == list1 or order == list1:  # check if the list = ordered list in both ways

            diff_list = [reverse_order[i] - reverse_order[i+1] for i in range(len(reverse_order) - 1)]  # cal the pair wise diff

            if any(x > 3 or x < 1 for x in diff_list):
                return False
            else:
                return True
        else:
            return False
    else:
        return False


def update_safe(list1):
    for n in range(len(list1)):
        temp_list = list1.copy()
        del temp_list[n]  # Remove the nth element
        if check_safe(temp_list):
            return True
    return False

# load data
reports = pd.read_excel('your input.xlsx', header=None, sheet_name = 'day2')
first_safe = reports.apply(check_safe, axis=1)
first_unsafe = reports[~first_safe]
second_safe = first_unsafe.apply(update_safe, axis=1)

print('first safe', first_safe.sum())  
print('second safe', first_safe.sum()+second_safe.sum())  
