
def bubbleSort(arr, update_visual_callback, quit_call):
    n = len(arr) 
    comparisons = 0
    array_accesses = 0
    for i in range(n):
        swapped = False
        for j in range (0, n-i-1):
            if quit_call():
                print("Stopping Algorithm")
                return

            comparisons += 1
            array_accesses += 2
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                swapped = True
                array_accesses += 4
                update_visual_callback(arr,j+1,[comparisons,array_accesses])
        if swapped == False:
            print("Algorithm Completed")
            break

