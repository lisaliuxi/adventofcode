with open('day 4.txt', 'r') as file:
    data = [list(line.strip()) for line in file]

# task 1
def is_valid_ind(data, ind, x_ind, deltas):
    for delta in deltas:
        new_row, new_col = ind + delta[0], x_ind + delta[1]
        if not (0 <= new_row < len(data) and 0 <= new_col < len(data[0])):
            return False
    return True


def check_sequence(data, ind, x_ind, deltas):
    if not is_valid_ind(data, ind, x_ind, deltas):
        return False
    return all(
        data[ind + delta[0]][x_ind + delta[1]] == char
        for delta, char in zip(deltas, "MAS")
    )


directions = {
    "horizontal_forward": [(0, 1), (0, 2), (0, 3)],
    "horizontal_backward": [(0, -1), (0, -2), (0, -3)],
    "vertical_down": [(1, 0), (2, 0), (3, 0)],
    "vertical_up": [(-1, 0), (-2, 0), (-3, 0)],
    "diag_down_right": [(1, 1), (2, 2), (3, 3)],
    "diag_up_right": [(-1, 1), (-2, 2), (-3, 3)],
    "diag_down_left": [(1, -1), (2, -2), (3, -3)],
    "diag_up_left": [(-1, -1), (-2, -2), (-3, -3)],
}

n = 0
for ind, row in enumerate(data):
    X_index_list = [i for i, x in enumerate(row) if x == 'X']
    for x_ind in X_index_list:
        for direction, deltas in directions.items():
            if check_sequence(data, ind, x_ind, deltas):
                n += 1

print(n)

# task 2
n = 0

for ind, row in enumerate(data):

    if ind not in [0, len(data) - 1]:  # A cant be in first / last row
        A_index_list = [i for i, x in enumerate(row) if x == 'A']

        for a_ind in A_index_list:
            if a_ind not in [0, len(row) - 1]:
                list_of_MS_1 = [data[ind - 1][a_ind - 1], data[ind + 1][a_ind + 1]]
                list_of_MS_2 = [data[ind - 1][a_ind + 1], data[ind + 1][a_ind - 1]]
                if sorted(list_of_MS_1) == ['M', 'S'] and sorted(list_of_MS_2) == ['M', 'S']:
                    n += 1

print(n)
