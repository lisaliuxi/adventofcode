import pandas as pd
import itertools

with open('day 8 test.txt', 'r') as file:
    rows = [list(line.strip()) for line in file]

# Convert the rows into a DataFrame
df = pd.DataFrame(rows)

# unique_values = pd.unique(df.values.ravel())
unique_values = set(df.values.flatten()) - {'.'}
print(unique_values)

def calculate_extended_nodes_within_bounds(indices, df, scale=1):
    """
    Calculate and append only nodes within the DataFrame bounds:
    1. A node forward in line with the second index at double the distance.
    2. A node backward in line with the first index at double the distance.

    Args:
    - indices (list of tuples): List of (row, col) indices.
    - df (DataFrame): DataFrame to check bounds against.

    Returns:
    - List of tuples containing (index1, index2, valid_node)
    """
    results = []
    max_row, max_col = df.shape  # Get dimensions of the DataFrame

    # Iterate through each pair of indices
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            index1 = indices[i]
            index2 = indices[j]

            # Calculate the vector
            vector = (index2[0] - index1[0], index2[1] - index1[1])

            # Forward node (from index2)
            forward_node = (index2[0] + scale*vector[0], index2[1] + scale*vector[1])
            if 0 <= forward_node[0] < max_row and 0 <= forward_node[1] < max_col:
                results.append(forward_node)

            # Backward node (from index1)
            backward_node = (index1[0] - scale*vector[0], index1[1] - scale*vector[1])
            if 0 <= backward_node[0] < max_row and 0 <= backward_node[1] < max_col:
                results.append(backward_node)

    return results

# part 1
all_antinodes = []
for uni in unique_values:
    indices_of_target = df.stack().loc[lambda x: x == uni].index.tolist()
    # print(indices_of_target)
    result = calculate_extended_nodes_within_bounds(indices_of_target, df)
    all_antinodes.append(result)

flattened_indices = [item for sublist in all_antinodes for item in sublist]
x = list(set(flattened_indices))

print(len(x))

all_antinodes = result = scale_list = []
for uni in unique_values:
    indices_of_target = df.stack().loc[lambda x: x == uni].index.tolist()
    for scale in range(0, 50):
        scale_list = calculate_extended_nodes_within_bounds(indices_of_target,df, scale)
        # result.append(scale_list)
        all_antinodes.append(scale_list)

flattened_indices = [item for sublist in all_antinodes for item in sublist]
x = list(set(flattened_indices))

print(len(x))

