import random
import math

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
    # Initialise variables 
    L = l   # L will be 0 or a value passed through by exponential search so should be set to l regardless of calling function. 

    if default:
        # Due to it coming from a exponential search, smaller subsection used to search through so R needs to be set and the search_value updated with the correct value.
        R = r
        search_value = x 
    else:
    # Not coming from exponential so a search value needs to be generated.
    # Right pointer to the end of the arr as will be searching through whole array
        R = len(arr) - 1
        search_value = random.randint(1, len(arr))
        print(f"Looking for: {search_value}")

    # While there are still elements between the pointers (ie the element could still be in the list)
    while L <= R:

        if quit_call(): # Prevents crashing and allows user to stop processing early.
            print("Stopping Algorithm")
            return False
        
        # Sets middle pointer
        middle = int((L+R) / 2)

        # Updates metrics & visual to show where the middle pointer is.
        metrics[0] += 1
        metrics[1] += 2

        update_visual_callback(arr, [middle],metrics)

        # Decides which sub-array should be searched next if the element is not at middle and sets the pointers accordingly.
        if arr[middle] > search_value:
            R = middle - 1
        elif arr[middle] < search_value:
            L = middle + 1
        else:
            # Return as element has been found (finished visual does not need to be ran so return False)
            print("Element Found")
            return False
    
    # Error has occured so return
    print("Error")
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
        if quit_call(): # Prevents crashing and allows user to stop processing early.
            print("Stopping Algorithm")
            return False
        
        x = random.randint(0,n - 1)

        comparisons += 1
        array_accesses += 1
        update_visual_callback(arr, [x],[comparisons,array_accesses])

        if arr[x] == search_value:
            print("Element Found")
            return False

def exponentialSearch(arr, update_visual_callback, quit_call):
    # Initialize variables.
    metrics = [0,0]
    n = len(arr)
    x = random.randint(1,len(arr))
    print(f"Looking for: {x}")

    # Check if the first element is the search value.
    if arr[0] == x:
        metrics = [metric + 1 for metric in metrics] 
        update_visual_callback(arr,[0],metrics)
        print("Element Found")
        return False
    
    
    i = 1

    # While the current indexed element is smaller then the search_value and the end of the arr has not been found, find the next exponential number.
    while i < n and arr[i] <= x:
        if quit_call(): # Prevents crashing and allows user to stop processing early.
            print("Stopping Algorithm")
            return False 
            
        i = i * 2

        metrics = [metric + 1 for metric in metrics]
        update_visual_callback(arr,[i],metrics)
    
    # Call a binary search with the smaller range of bounds given by the exponential search.
    # Using the found exponentials number, set the lower bound the be 1/2 * e, and upper bound being the exponential number or the end of the arr. 
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

def insertionSort(arr, update_visual_callback, quit_call):
    # Initialising variables
    metrics = [0,0]
    n = len(arr)
    i = 1

    # Loop over all elements in the array
    while i < n:
        if quit_call(): # Prevents crashing and allows user to stop processing early.
            print("Stopping Algorithm")
            return False
        
        # Set a temp variable x to hold the current element (so it can be moved to the correct location)
        x = arr[i]
        # Set another pointer to the next element to be inserted into the sorted arr.
        j = i

        metrics[1] += 1

        # Loop backwords through the sorted array to find where the element should be located.
        while j > 0 and arr[j-1] > x:
            if quit_call(): # Prevents crashing and allows user to stop processing early.
                print("Stopping Algorithm")
                return False

            metrics[0] += 1 # Update comparisons metric
            metrics[1] += 3 # Update array accesses metric
            
            # Shift all elements to the right one so that when the correct location for the focused element has been found, it can overwrite the current element in that location. 
            arr[j] = arr[j-1]
            j -= 1

            update_visual_callback(arr,[i,j], metrics)  # Update the visual
        
        # Set the correct location to the currently focused element and move onto the next element in the array.
        arr[j] = x
        i += 1

        metrics[1] += 1 # Update array accesses metric
        update_visual_callback(arr, [i], metrics)   # Update the visual 

    
    return True

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

def heapSort(arr, update_visual_callback, quit_call):
    metrics = [0,0]
    
    def sort(arr):
        n = len(arr)

        # Build max heap 
        for i in range((n // 2) - 1 ,-1,-1):
            if not heapify(arr,n,i):
                return False

        # Extract max elements from the heap and place in the "sorted" section of the array. 
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap placing biggest element in the heap in the arr at i
            
            metrics[1] += 4 # Update metrics.

            if not heapify(arr, i, 0):  # Fix heap to find new biggest element
                return True

            if quit_call(): # Prevents crashing and allows user to stop processing early.
                print("Stopping Algorithm")
                return False
            
            update_visual_callback(arr,[i],metrics) # Update visual with sorted subsection growth.
        
        return True

    def heapify(arr,n, i):
        max = i # The biggest element should be at i (on first run, the biggest is the first element )

        # Pointers to the left and right child in the heap
        left  = (2 * i) + 1        
        right = (2 * i) + 2

        # If the left child is greater then the root, max needs to be the left child.
        if left < n and arr[max] < arr[left]:
            max = left
        
        # If the right child is greater then the root max needs to be the right child. 
        if right < n and arr[max] < arr[right]:
            max = right

        # Update metrics
        metrics[0] += 2
        metrics[1] += 4
        
        # Ensure the root is the biggest element (if the max pointer has changed to one of the child nodes)
        if max != i:
            metrics[1] += 4

            arr[i], arr[max] = arr[max], arr[i]
            
            if quit_call(): # Prevents crashing and allows user to stop processing early.
                print("Stopping Algorithm")
                return False
            update_visual_callback(arr,[i],metrics) # Update visual with heap creation 
            # heapify the root
            if not heapify(arr,n,max):
                return False
            
        return True

    if not sort(arr):
        return False
    update_visual_callback(arr,[0],metrics)
    return True

def countingSort(arr, update_visual_callback, quit_call):
    #Initialise variables
    k = len(arr)
    metrics = [0,0]

    # Counting sort is very bad sort for when there are no repeats in the data. 

    input_arr = arr.copy()      # Create a copy of the original arr so arr can be overwritten for the visual.
    count_arr = [0] * (k+1)     # Create a count array to keep track of how many times a number appears (Due to algorithm_visualiser will be a full array with 1 as every element)

    # Iterate over all the numbers in the array and increment the count for that element in the count array.
    for num in arr:
        count_arr[num] += 1
        metrics[1] += 1


    # Calculate the prefix sum, so the location for the element can be found.
    for i in range(1,k+1):
        count_arr[i] += count_arr[i - 1]

    # Superimpose the input_arr onto the arr using the count_arr
    for i in range(k-1,-1,-1):
        if quit_call(): # Prevents crashing and allows user to stop processing early.
            print("Stopping Algorithm")
            return False

        arr[count_arr[input_arr[i]] - 1] = input_arr[i]
        count_arr[input_arr[i]] -= 1

        metrics[1] += 3
        update_visual_callback(arr,[i],metrics)       # Update visual

    return True

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

def quickSort(arr, update_visual_callback, quit_call):
    # Initialize variables
    metrics = [0,0]

    def sort(arr, low_index, high_index):
        # Set the pointers to the start of subarray, end of syb array and pivot in the middle
        left = low_index
        right = high_index
        pivot = arr[(low_index + high_index) // 2]

        metrics[1] += 1

        # While the left pointer is still small then right pointer 
        while left <= right:
            if quit_call(): # Prevents crashing and allows user to stop processing early.
                print("Stopping Algorithm")
                return False
            
            #  Ensure all the elements to the left of the pivot are smaller then the pivot element
            while arr[left] < pivot and left < high_index:
                if quit_call(): # Prevents crashing and allows user to stop processing early.
                    print("Stopping Algorithm")
                    return False
            
                left += 1
                metrics[0] += 1
                metrics[1] += 1
            metrics[1] += 1

            # Ensure all the elements to the right of the pivot are greater then the pivot.
            while pivot < arr[right] and right > low_index:
                if quit_call(): # Prevents crashing and allows user to stop processing early.
                    print("Stopping Algorithm")
                    return False

                right -= 1

                metrics[0] += 1
                metrics[1] += 1
            metrics[1] += 1
            
            if left <= right:
                # Swap the elements which are not on the correct side of the pivot and move pointers onto next element.
                x = arr[left]
                arr[left] = arr[right]
                arr[right] = x

                left += 1
                right -= 1

                metrics[1] += 4

            
            update_visual_callback(arr, [left,pivot,right],metrics)

        # Recurse with the left section of the pivot & right of pivot to sort the whole array. 
        if low_index < right: 
            if not sort(arr, low_index, right):
                return False
        if right < high_index: 
            if not sort(arr, left, high_index):
                return False

        return True



    if not sort(arr,0, len(arr) - 1):
        return False
    else:
        return True 

def selectionSort(arr, update_visual_callback, quit_call):
    # Initialise variables
    n = len(arr)
    metrics= [0,0]

    for i in range(n - 1):
        j_min = i

        # Search the rest of the array to find the next smallest element.
        for j in range(i+1,n):
            metrics[0] += 1
            metrics[1] += 2

            if arr[j] < arr[j_min]:
                j_min = j

            if quit_call(): # Prevents crashing and allows user to stop processing early.
                print("Stopping Algorithm")
                return False
            update_visual_callback(arr, [j,i], metrics) # Update visual, make processing look quicker. 

        if j_min != i:
            # Swap the selected smallest element (j_min) to i [the current focused element to be found] & update metrics.
            metrics[1] += 4  
            arr[i], arr[j_min] = arr[j_min], arr[i]

            # Updating Visual
            if quit_call(): # Prevents crashing and allows user to stop processing early.
                print("Stopping Algorithm")
                return False
            update_visual_callback(arr, [j,i], metrics)

    return True

def radixSort(arr,update_visual_callback, quit_call):
    # Initialise metrics
    metrics = [0,0]

    # Driver counting sort
    def counting_sort(arr, exp1):
        n = len(arr)

        # Copy the array so it can be overwritten (for the visual)
        input_arr = arr.copy()
        count = [0] * 10    # Declare a count array for all the digits 0-9.

        for i in range(0, n):
            index = input_arr[i] // exp1    # Get the current digit from the current element 
            count[index % 10] += 1          # Increase the count for that digit.

            metrics[1] += 1

        # Prefix sum the counts so the location for elements can be determined. 
        for i in range(1,10):
            count[i] += count[i - 1]

        # Build the output array based of the count 
        i = n - 1
        while i >= 0:
            index = input_arr[i] // exp1                # Get the index of the current elements digit so it can be searched in count to determine location. 
            arr[count[index % 10] - 1] = input_arr[i]   # Overwrite the element to the correct location in the array
            count[index % 10] -= 1

            # Handle UI
            metrics[1] += 3
            if quit_call(): # Prevents crashing and allows user to stop processing early.
                print("Stopping Algorithm")
                return False
            update_visual_callback(arr,[i],metrics)
            
            i -= 1 

        return True


    # Radix Sort.
    def sort(arr):
        # Finds the biggest number in the array [to find number of digits in it]
        max1 = max(arr)

        exp = 1 # Initialise current exponent 10^i [where i = 1 atm]
        
        # Repeat counting sort for every digit in the biggest number in the array.
        while max1 / exp >= 1:
            if not counting_sort(arr, exp):     # Do counting sort on the current exponent [digit]
                return False
            exp *= 10                           # Increase exponent by factor of 10 to do counting sort on the next digit.
        
        return True
    
    if not sort(arr):
        return False
    else:
        return True