import random
import math

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

def binarySearch(arr, update_visual_callback, quit_call):
    comparisons = 0
    array_accesses = 0
    search_value = random.randint(1, len(arr))
    print(f"Lookign for: {search_value}")
    L = 0
    R = len(arr) - 1

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
        print("Element Found ")
        return False

    print("Error: Element not found in the array.")
    return False


