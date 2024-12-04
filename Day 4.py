with open('day 4.txt', 'r') as file:
    data = [list(line.strip()) for line in file]

# task 1

n = 0
for ind, row in enumerate(data):
    X_index_list = [i for i, x in enumerate(row) if x == 'X']
    
    for x_ind in X_index_list:
        # 1. forward - 
        if x_ind <= len(row)-4: #horizontal
            if data[ind][x_ind+1] == 'M':
                if data[ind][x_ind+2] == 'A':
                    if data[ind][x_ind+3] == 'S':
                        n += 1
            if ind <= len(data)-4: #right bottom diag
                if data[ind+1][x_ind+1] == 'M':
                    if data[ind+2][x_ind+2] == 'A':
                        if data[ind+3][x_ind+3] == 'S':
                            n += 1
            if ind >= 3: #right up diag
                if data[ind-1][x_ind+1] == 'M':
                    if data[ind-2][x_ind+2] == 'A':
                        if data[ind-3][x_ind+3] == 'S':
                            n += 1
        # 2. backwards 
        if x_ind >= 3: #horizontal
            if data[ind][x_ind-1] == 'M':
                if data[ind][x_ind-2] == 'A':
                    if data[ind][x_ind-3] == 'S':
                        n += 1 
            if ind <= len(data)-4: #left bottom diag
                if data[ind+1][x_ind-1] == 'M':
                    if data[ind+2][x_ind-2] == 'A':
                        if data[ind+3][x_ind-3] == 'S':
                            n += 1           
            if ind >= 3: #left up diag
                if data[ind-1][x_ind-1] == 'M':
                    if data[ind-2][x_ind-2] == 'A':
                        if data[ind-3][x_ind-3] == 'S':
                            n += 1
        
        # 2. vertical
        if ind <= len(data)-3:
            if data[ind+1][x_ind] == 'M':
                if data[ind+2][x_ind] == 'A':
                    if data[ind+3][x_ind] == 'S':
                        n += 1
        if ind >=3:
            if data[ind-1][x_ind] == 'M':
                if data[ind-2][x_ind] == 'A':
                    if data[ind-3][x_ind] == 'S':
                        n += 1
# task 2
n = 0

for ind, row in enumerate(data): 
    
    if ind not in [0, len(data)-1]:  # A cant be in first / last row
        A_index_list = [i for i, x in enumerate(row) if x == 'A']
        
        for a_ind in A_index_list:
            if a_ind not in [0, len(row)-1]: 
                list_of_MS_1 = [data[ind-1][a_ind-1], data[ind+1][a_ind+1]]
                list_of_MS_2 = [data[ind-1][a_ind+1], data[ind+1][a_ind-1]]
                if sorted(list_of_MS_1) == ['M', 'S'] and sorted(list_of_MS_2) == ['M', 'S']:
                    n+=1
