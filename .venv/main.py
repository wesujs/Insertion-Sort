def insertion_sort(arr):
    # Loop through each element in the array starting from the second one
    for i in range(1, len(arr)):
        print(f"Starting arr is: {arr}")
        key = arr[i]
        print("---- key at start: ", key, "\n---- i index at start: ", i)# The current element to be inserted
        j = i - 1
        print("---- j index at start: ", j)

        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        print(f"Is {j} >= 0 and is {arr[j]} > {key}")
        while j >= 0 and arr[j] > key:
            print("---- j index at beginning of while: ", j)
            arr[j + 1] = arr[j]
            print(f"------ arr[{j + 1}] is assigned {arr[j]}")
            j -= 1
            print("---- j index at end: ", j)
            print("--- arr[j] at end: ", arr[j])
            if (j >= 0) == False:
                print(f"j:{j} was less than 0, so while loop was exited----")
            elif (arr[j] > key) == False:
                print(f"arr[j]:{arr[j]} was less than key:{key} so while loop was exited----")

        # Place the key in its correct position
        arr[j + 1] = key
        print(f"Sets arr[{ j + 1}] to {key}\nSo current arr is {arr}")
        print("LOOP IS OVER-----------------")


# Example usage
numbers = [5, 2, 4, 6, 1, 3, 7]
insertion_sort(numbers)
print("Sorted array:", numbers)
