** start of main.py **

def selection_sort(arr):
    # Loop through each position in the list
    for i in range(len(arr)):
        # Assume the current position holds the minimum
        min_index = i

        # Find the index of the smallest element in the unsorted part
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap only if a smaller element was found
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    # Return the same list (sorted in-place)
    return arr


** end of main.py **

