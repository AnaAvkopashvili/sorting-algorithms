# Implement several sorting and searching algorithms
# Do NOT use any built in function except len and range

""" Insertion Sort """


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# The given code is an implementation of the insertion sort algorithm. Insertion sort is a simple sorting algorithm
# that builds the final sorted array one element at a time.
#
# Here's how the insertion sort algorithm works:
#
# The insertion_sort function takes an array arr as input.
# It starts iterating from the second element (i = 1) to the last element of the array.
# For each iteration, it assigns the current element to the variable key.
# It initializes a variable j with the value i - 1 to keep track of the element before the current element.
# It enters a while loop that continues until j is greater than or equal to 0 and the key is less than
# the element at position j.
# Inside the while loop, it shifts the element at position j one position to the right (i.e., arr[j + 1] = arr[j]).
# It decrements j by 1 to check the previous element in the next iteration.
# Once the while loop terminates, it inserts the key into its correct position in the sorted sequence by
# assigning it to arr[j + 1].
# The process continues until all elements in the array are sorted.
# The code sorts the input array in-place using the insertion sort algorithm. After the function execution,
# the array arr will be sorted in ascending order.



""" Selection Sort """


def selection_sort(arr):
    N = len(arr)
    for i in range(N):
        k = i
        for j in range(i + 1, N):
            if arr[k] > arr[j]:
                k = j
        arr[i], arr[k] = arr[k], arr[i]

# The given code is an implementation of the selection sort algorithm. Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the array and placing it at the beginning of the sorted part.
#
# Here's how the selection sort algorithm works:
#
# The selection_sort function takes an array arr as input.
# It initializes a variable N with the length of the array.
# It starts iterating from the first element (i = 0) to the second-to-last element of the array.
# For each iteration, it assumes the current element at index i as the minimum element (k = i).
# It then starts an inner loop from the next element (j = i + 1) to the last element of the array.
# Inside the inner loop, it compares the element at index k with the element at index j.
# If the element at index k is greater than the element at index j, it updates the value of k to j, indicating that the element at index j is the new minimum.
# After the inner loop completes, it swaps the minimum element (arr[k]) with the element at index i using a simultaneous assignment (arr[i], arr[k] = arr[k], arr[i]).
# This places the minimum element in its correct sorted position at the beginning of the array.
# The process continues until all elements in the array are sorted.

""" Merge Sort """


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# The given code is an implementation of the merge sort algorithm. Merge sort is a divide-and-conquer sorting algorithm that recursively divides the array into two halves, sorts them separately, and then merges the sorted halves to obtain the final sorted array.
#
# Here's how the merge sort algorithm works:
#
# The merge_sort function takes an array arr as input.
# It checks if the length of the array is greater than 1, which is the base case for the recursion.
# If the length of the array is greater than 1, it calculates the midpoint (mid) of the array using integer division (//).
# It then divides the array into two halves: the left half (L) from index 0 to mid-1, and the right half (R) from index mid to the end of the array.
# The merge_sort function is called recursively on both the left and right halves, which further divides them into smaller subarrays until the base case is reached.
# After the recursive calls, the function proceeds to merge the sorted left and right halves back into the original array.
# It initializes three variables i, j, and k to keep track of the indices for the left half, right half, and the merged array, respectively.
# It enters a while loop that continues as long as both i and j are within the bounds of their respective halves.
# Inside the while loop, it compares the elements at indices i and j in the left and right halves, respectively.
# If the element in the left half (L[i]) is smaller than the element in the right half (R[j]), it assigns the element from the left half to the current position in the merged array (arr[k] = L[i]) and increments i and k by 1.
# If the element in the right half is smaller or equal, it assigns the element from the right half to the current position in the merged array and increments j and k by 1.
# After the while loop, there might be some remaining elements in either the left or right half. The code uses two additional while loops to handle these cases and copy any remaining elements into the merged array.
# Finally, the merge sort algorithm is complete, and the original array arr is sorted.


""" Quick Sort """


def partition(arr, start, end):
    pivot_index, pivot = end, arr[end]
    left_index = start
    for i in range(start, end + 1):
        if arr[i] < pivot:
            arr[i], arr[left_index] = arr[left_index], arr[i]
            left_index += 1
    arr[pivot_index], arr[left_index] = arr[left_index], arr[pivot_index]
    return left_index

print(partition([1,4,3,2,5], 0, 4))

def quick_sort_aux(arr, start, end):
    if (start < end):
        p = partition(arr, start, end)
        quick_sort_aux(arr, start, p - 1)
        quick_sort_aux(arr, p + 1, end)


def quick_sort(arr):
    quick_sort_aux(arr, 0, len(arr) - 1)


# The given code is an implementation of the quicksort algorithm. Quicksort is a divide-and-conquer sorting algorithm that works by selecting a pivot element from the array and partitioning the other elements into two subarrays, according to whether they are less than or greater than the pivot. The subarrays are then recursively sorted.
#
# Here's how the quicksort algorithm works:
#
# The partition function takes an array arr, a start index start, and an end index end as input.
# It selects the pivot element as the element at the end index and stores its value in the variable pivot.
# It initializes left_index with the value of start, which keeps track of the index where elements less than the pivot will be placed.
# It iterates from start to end using a for loop.
# Inside the loop, it compares each element arr[i] with the pivot.
# If arr[i] is less than the pivot, it swaps the element at index i with the element at left_index and increments left_index by 1.
# This effectively moves all elements less than the pivot to the left side of the array.
# After the loop finishes, it swaps the pivot element with the element at left_index. Now, the pivot element is in its final sorted position in the array.
# The partition function returns the index of the pivot element.
# The quick_sort_aux function is a helper function that performs the recursive sorting of the subarrays.
# It takes an array arr, a start index start, and an end index end as input.
# If start is less than end, it calls the partition function to obtain the pivot index p.
# It recursively calls quick_sort_aux for the subarray to the left of the pivot (start to p - 1) and the subarray to the right of the pivot (p + 1 to end).
# The quick_sort function is the entry point for the quicksort algorithm.
# It calls quick_sort_aux with the initial values of start as 0 and end as len(arr) - 1, which represents the entire array.


""" Counting Sort """


def count_sort(arr):
    if arr == []:
        return

    mx = arr[0]
    for x in arr:
        if x > mx:
            mx = x

    count = [0 for i in range(mx + 1)]

    for x in arr:
        count[x] += 1
    count_index = 0
    for index in range(len(arr)):
        while count[count_index] == 0:
            count_index += 1
        arr[index] = count_index
        count[count_index] -= 1

arr = [5, 9, 1, 6, 10, 3]
count_sort(arr)
print(arr)


# The given code is an implementation of the count sort algorithm. Count sort is a non-comparative sorting algorithm that works by determining the number of occurrences of each distinct element in the input array and using this information to construct the sorted array.
#
# Here's how the count sort algorithm works:
#
# The count_sort function takes an array arr as input.
# It checks if the array is empty. If it is, the function returns since there is nothing to sort.
# It initializes a variable mx with the first element of the array, which represents the maximum element in the array.
# It iterates through the array to find the maximum element. This is done to determine the size of the count array.
# It initializes a count array of size mx + 1 with all elements set to 0. The count array will be used to store the count of each element.
# It iterates through the array again and increments the count for each element in the count array.
# It initializes a variable count_index with 0, which represents the index of the count array.
# It iterates through the original array using a nested loop.
# Inside the loop, it finds the first non-zero count in the count array by incrementing count_index until a non-zero count is found.
# It assigns the current count_index value to the element in the original array and decrements the count for that index in the count array.
# This process is repeated for all elements in the original array, resulting in a sorted array.
# After the loop completes, the original array will be sorted in ascending order.


# ------------- Search -------------

""" Jump Search """


def jump_search(x, step, arr):
    curr = step
    n = len(arr)
    while arr[min(curr, n - 1)] < x:
        if curr >= n:
            return -1
        curr += step

    for i in range(max(curr - step + 1, 0), min(curr + 1, n)):
        if arr[i] == x:
            return i

    return -1


# The given code is an implementation of the jump search algorithm. Jump search is a search algorithm that works on sorted arrays and is an improvement over the linear search algorithm. It jumps ahead by a fixed step to quickly reduce the search range and then performs a linear search within that range.
#
# Here's how the jump search algorithm works:
#
# The jump_search function takes three parameters: the element to search for x, the jump step step, and the sorted array arr.
# It initializes a variable curr with the value of step, which represents the current index to start the search.
# It calculates the length of the array n.
# It enters a while loop that continues as long as the element at index min(curr, n - 1) in the array is less than x.
# Inside the loop, it checks if curr has reached or exceeded the length of the array (curr >= n). If it has, it means the element is not present in the array, so the function returns -1 to indicate that the element was not found.
# If the element at index min(curr, n - 1) is less than x, it means the search should continue, and curr is updated by adding the step value.
# Once the while loop exits, it means the element is now within a possible range, and a linear search is performed within that range.
# The linear search is performed from the index max(curr - step + 1, 0) to the index min(curr + 1, n). The purpose of using max and min is to ensure that the search range remains within the bounds of the array.
# If the element is found during the linear search, the function returns its index.
# If the element is not found within the search range, the function returns -1 to indicate that the element was not found.


""" Binary Search """


def binary_search_aux(x, arr, left, right):
    if right >= left:
        mid = (right + left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_aux(x, arr, left, mid - 1)
        else:
            return binary_search_aux(x, arr, mid + 1, right)
    else:
        return -1


def binary_search(x, arr):
    return binary_search_aux(x, arr, 0, len(arr) - 1)

# The given code provides an implementation of the binary search algorithm. Binary search is a search algorithm that works on sorted arrays by repeatedly dividing the search interval in half until the target element is found or the search interval is empty.
#
# Here's how the binary search algorithm works:
#
# The binary_search_aux function is a recursive helper function that takes four parameters: the element to search for x, the sorted array arr, the left index of the search interval left, and the right index of the search interval right.
# It checks if right is greater than or equal to left. If it is, there is still a valid search interval to consider.
# It calculates the middle index of the search interval using the formula mid = (right + left) // 2.
# It compares the element at the middle index arr[mid] with the target element x.
# If arr[mid] is equal to x, it means the target element has been found, and the function returns the index mid.
# If arr[mid] is greater than x, it means the target element must be located in the left half of the search interval. The binary_search_aux function is recursively called with the updated right index mid - 1 to search in the left half.
# If arr[mid] is less than x, it means the target element must be located in the right half of the search interval. The binary_search_aux function is recursively called with the updated left index mid + 1 to search in the right half.
# If the base condition of right >= left is not met, it means the target element is not found in the array, and the function returns -1 to indicate that the element was not found.
# The binary_search function is the entry point for the binary search algorithm. It calls the binary_search_aux function with the initial values of left as 0 and right as len(arr) - 1, which represents the entire array.
# The binary_search function returns the result of the binary_search_aux function.