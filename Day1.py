import pandas as pd
import numpy as np

list_id = pd.read_excel('your input.xlsx', header=None, sheet_name = 'day1')

list_id_left = list_id[0].to_list()
list_id_right = list_id[1].to_list()

list_id_left.sort()
list_id_right.sort()

# part 1
diff = 0

for left, right in zip(list_id_left, list_id_right):
    diff += abs(left - right)
print('diff is', str(diff))

# part 2
from collections import Counter

sim = 0

value_counts = Counter(list_id_left)
for value, count in value_counts.items():    
    if value in list_id_right:
        count_in_right = list_id_right.count(value)
        sim += value * count * count_in_right
    else:
        pass

print('sim score is', str(sim))
