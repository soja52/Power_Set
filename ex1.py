
def possible_subsets(arr):
    n = len(arr)
    total_subsets = 1 << n   # 2^n

    for i in range(total_subsets):
        subset = []

        for j in range(n):

            # Check if jth bit is set
            if i & (1 << j):
                subset.append(arr[j])

        print(subset)


# Example usage
arr = ['a', 'b', 'c']
possible_subsets(arr)
