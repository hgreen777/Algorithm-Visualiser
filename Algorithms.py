import random
import math

"""TODO"""
#TODO : Clean algorithms code (binary search & exponential binarysearch)
#TODO : Insertion Sort
#TODO : Merge Sort - comments
#TODO : Heap Sort
#TODO : Counting Sort
#TODO : Quick Sort 

"""SEARCHING ALGORITHMS"""
def linearSearch(arr, update_visual_callback, quit_call):
    comparisons = 0
    array_accesses = 0
    searchValue = random.randint(1, len(arr))

    print(f"looking for: {searchValue}")
    for i in range(len(arr)):
        if quit_call():
            print("Stopping Algorithm")
            return False
        
        array_accesses += 1
        comparisons += 1

        update_visual_callback(arr,[i],[comparisons,array_accesses])
        if arr[i] == searchValue:
            print("Element Found")
            return False
    
    print("Error: Element not in array")
    return False

def binarySearch(arr, update_visual_callback, quit_call, l=0,r=0,x=0,metrics=[0,0],default=False):
    comparisons = 0
    array_accesses = 0
    search_value = random.randint(1, len(arr))
    L = l
    if default:
        R = r
        search_value = x 
        comparisons = metrics[0]
        array_accesses = metrics[1]
    else:
        R = len(arr) - 1
        print(f"Lookign for: {search_value}")

    while L <= R:
        if quit_call():
            print("Stopping Algorithm")
            return False
        
        middle = int((L+R) / 2)
        comparisons += 1
        array_accesses += 2

        update_visual_callback(arr, [middle],[comparisons,array_accesses])
        if arr[middle] > search_value:
            R = middle - 1
        elif arr[middle] < search_value:
            L = middle + 1
        else:
            print("Element Found")
            return False
        
def jumpSearch(arr, update_visual_callback, quit_call):
    # Requires Sorted Array
    comparisons = 0
    array_accesses = 0
    n = len(arr)
    search_value = random.randint(1,n)
    print(f"looking for: {search_value}")

    i = 0 
    b = int(math.floor(math.sqrt(n)))

    while arr[min(b, n) - 1] < search_value:
        if quit_call():
            print("Stopping Algorithm")
            return False
        array_accesses += 1
        comparisons += 1
        
        i = b
        b = b + int(math.floor(math.sqrt(n)))

        if i >= n:
            print("Error: Element not found in the array")
            return False
        
        update_visual_callback(arr,[i],[comparisons,array_accesses])
    
    comparisons += 1
    array_accesses += 1

    while arr[i] < search_value:
        if quit_call():
            print("Stopping Algorithm")
            return False 
        array_accesses += 1
        comparisons += 1
        
        i += 1
        if i == min(b,n):
            print("Error: Element not found in the array.")
            return False
        
        update_visual_callback(arr,[i],[comparisons,array_accesses])
    
    comparisons += 2
    array_accesses += 2
    if arr[i] == search_value:
        update_visual_callback(arr,[i],[comparisons,array_accesses])
        print("Element Found ")
        return False

    print("Error: Element not found in the array.")
    return False

def bogoSearch(arr, update_visual_callback, quit_call):
    comparisons = 0
    array_accesses = 0
    n = len(arr)
    search_value = random.randint(1,n)
    print(f"looking for: {search_value}")

    x = 0
    found = False

    while not found:
        if quit_call():
            print("Stopping Algorithm")
        
        x = random.randint(0,n - 1)

        comparisons += 1
        array_accesses += 1
        update_visual_callback(arr, [x],[comparisons,array_accesses])

        if arr[x] == search_value:
            print("Element Found")
            return False

def exponentialSearch(arr, update_visual_callback, quit_call):
    metrics = [0,0]
    n = len(arr)
    x = random.randint(1,len(arr))
    print(f"Looking for: {x}")

    if arr[0] == x:
        metrics = [metric + 1 for metric in metrics] 
        update_visual_callback(arr,[0],metrics)
        print("Element Found")
        return False
    
    
    i = 1

    while i < n and arr[i] <= x:
        if quit_call():
            print("Stopping Algorithm")
            return False 
            
        i = i * 2

        metrics = [metric + 1 for metric in metrics]
        update_visual_callback(arr,[i],metrics)
    
    #return binarySearchh(arr, i // 2, min(i, n-1),x, metrics, update_visual_callback, quit_call)
    return binarySearch(arr, update_visual_callback, quit_call,i // 2,min(i,n-1),x,metrics,True)

def fibonacciSearch(arr, update_visual_callback, quit_call):
    metrics = [0,0]
    n = len(arr)
    x = random.randint(1,n)
    print(f"looking for: {x}")

    # Calculating valid fibonacci sequence for the array.
    k = 3
    F = [0,1,1]
    while F[k - 1] < n:
        F.append(F[k-1] + F[k-2])
        k += 1

    # Check valid array is passed
    if k <= 1:
        print("Error: Array is not of valid length")
        return False
    
    found = False
    offset = -1 

    # Search until elements is found or program crashes due to infinite loop.
    while not found:
        # For exiting algo early.
        if quit_call():
            print("Stopping Algorithm")
            return False
        
        # Checking either the 
        i = min(offset + F[k - 2], n - 1)

        update_visual_callback(arr,[i], metrics)
        if x == arr[i]: # Element is found 
            found = True
            print(f"Element Found at {arr[i]}")
            return False
        if x > arr[i]: # If the element is not in that fibonacci gap (but it is to the right)
            k = k -1 
            offset = i
        if x < arr[i]:
            k = k - 2

    print("Error")
    return False

"""SORTING ALGORITHMS"""      
def bubbleSort(arr, update_visual_callback, quit_call):
    n = len(arr) 
    comparisons = 0
    array_accesses = 0
    for i in range(n):
        swapped = False
        for j in range (0, n-i-1):
            if quit_call():
                print("Stopping Algorithm")
                return False

            comparisons += 1
            array_accesses += 2
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                swapped = True
                array_accesses += 4

                update_visual_callback(arr,[j,j+1],[comparisons,array_accesses])
        if swapped == False:
            print("Algorithm Completed")
            return True

# TODO
def insertionSort(arr, update_visual_callback, quit_call):
    return False

def mergeSort(array, update_visual, quit_call):
    metrics = [0,0]

    # Responsible for merging 2 subarrays togethor.
    def merge(arr, left, mid, right):
        n1 = mid - left + 1         # Size of L array
        n2 = right - mid            # Size of R array

        L = arr[left:mid + 1]       # Creates a left array
        R = arr[mid + 1:right + 1]  # Creates a right array

        i = j = 0   # creates 2 left pointers for the start of the L & R array.
        k = left    # Creates a pointer to index of the location for the enxt sorted elements.

        metrics[1] += 2

        # While the pointers have not reached the end of each of the arrays.
        while i < n1 and j < n2:
            if quit_call(): # Prevents crashing and allows user to stop processing early.
                print("Stopping Algorithm")
                return False
            metrics[0] += 1
            metrics[1] += 4


            # If the current element of the left subarray is smaller then the current pointed to right array element, add the left element to that position in the array and move the left pointer by 1.
            if L[i] <= R[j]:
                arr[k] = L[i]

                update_visual(arr, [k, left + i], metrics)

                i += 1
            else:
            # Else set the current element to be where the right pointer is and move the right pointer along.
                arr[k] = R[j]

                update_visual(arr, [k, mid + 1 + j], metrics)

                j += 1
            
            # Move onto the next element in the main array.
            k += 1

        # For the rest of the left array, set the next element to the next element in the array (this means all the right array is smaller then the rest of the left array).
        while i < n1:
            if quit_call(): # Prevents crashing and allows user to stop processing early.
                print("Stopping Algorithm")
                return False
            metrics[1] += 2
            
            arr[k] = L[i]

            update_visual(arr, [k, left + i], metrics)

            i += 1
            k += 1

        # For the rest of the right array, set the next element to the next element in the array (this means all the left array is smaller then the rest of the right array).
        while j < n2:
            if quit_call(): # Prevents crashing and allows user to stop processing early.
                print("Stopping Algorithm")
                return False
            metrics[1] += 2

            arr[k] = R[j]

            update_visual(arr, [k, mid + 1 + j], metrics)

            j += 1
            k += 1
        
        return True

    # Responsible for splitting the array down into sub arrays & then merging the subarrays togethor but in a sorted fashion.
    def merge_sort_recursive(arr, left, right):
        # Until the whole of the array has been split into it's smallest array [ie 1]
        if left < right:
            mid = (left + right) // 2   # Find the middle to create 2 subarrays left,middle & middle,right

            # Recurse until len(arr) = 1
            if not merge_sort_recursive(arr, left, mid):
                return False
            if not merge_sort_recursive(arr, mid + 1, right):
                return False

            update_visual(arr, list(range(left, right + 1)), metrics)
            if not merge(arr, left, mid, right):
                return False

        return True

    update_visual(array, list(range(len(array))), metrics)
    # Start the merge sort on the whole array.
    if not merge_sort_recursive(array, 0, len(array) - 1):
        return False
    return True

# TODO
def heapSort(arr, update_visual_callback, quit_call):
    return False

# TODO
def countingSort(arr, update_visual_callback, quit_call):
    return False

def bogoSort(arr, update_visual_callback, quit_call):
    n = len(arr)
    metrics = [0,0]

    """ Randomly shuffles the array by changing the position of every element. """
    def shuffleArray(n,arr):
        n -= 1

        for i in range(0, n):
            j = random.randint(0, n)
            arr[i], arr[j] = arr[j], arr[i]
        
        metrics[1] += (n + 1) * 4
        

    """ Checks if the array is sorted. """
    def array_sorted(arr):
        j = 1
        sorted = True

        # Linearly traverses array to ensure it is ordered.
        for i in range(0, n):
            metrics[1] += 1
            if arr[i] != j:
                return False
            
            j += 1
        
        return True
    
    # While the array is not sorted, shuffle the array (and update visual).
    while not array_sorted(arr):
        if quit_call(): # Prevents crashing and allows user to stop processing early.
            print("Stopping Algorithm")
            return False
        
        shuffleArray(n,arr)
        
        # Updates comparisons and produces a visual update on the screen.
        metrics[0] += 1
        update_visual_callback(arr,[0],metrics)
    
    # Array has been sorted.
    return True

# TODO 
def quickSort(arr, update_visual_callback, quit_call):
    return False 