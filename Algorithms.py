import random
import math

"""TODO"""
#TODO : Clean algorithms code (binary search & exponential binarysearch)
#TODO : Insertion Sort
#TODO : Merge Sort
#TODO : Heap Sort
#TODO : Counting Sort
#TODO : Bogo Sort

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

# TODO
def mergeSort(arr, update_visual_callback, quit_call):
    metrics = [0,0]
    n = len(arr)

    def copy_array(a,i_begin,i_end,b):
        for k in range(i_begin,i_end):
            b.append(a[k])
        
        return b    

    def top_down_merge(b, i_begin, i_middle, i_end,a):
        i = i_begin
        j = i_middle

        for k in range(i_begin, i_end):
            update_visual_callback(b,[i_begin,i_end,k,i,j],metrics)
            if i < i_middle and (j >= i_end or a[i] <= a[j]):
                b[k] = a[i]
                i += 1
            else:
                b[k] = a[j]
                j += 1
        
        return b

    def top_down_split_merge(b, i_begin, i_end, a):
        if (i_end - i_begin) <= 1:
            return
        
        i_middle = (i_begin + i_end) // 2

        update_visual_callback(arr,[i_begin,i_end], metrics)

        top_down_split_merge(a,i_begin,i_middle,b)
        top_down_split_merge(a,i_middle,i_end,b)

        return top_down_merge(b,i_begin, i_middle, i_end, a)

        

    def top_down_merge_sort(a,b,n):
        b = copy_array(a,0,n,b)
        return top_down_split_merge(a,0,n,b)
    
    update_visual_callback(top_down_merge_sort(arr,[],n),[n-1],metrics)
    return True

# TODO
def heapSort(arr, update_visual_callback, quit_call):
    return False

# TODO
def countingSort(arr, update_visual_callback, quit_call):
    return False

# TODO
def bogoSort(arr, update_visual_callback, quit_call):
    return False