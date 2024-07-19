
def bubbleSort(arr, update_visual_callback, quit_call):
    n = len(arr) 
    comparisons = 0
    for i in range(n):
        swapped = False
        for j in range (0, n-i-1):
            if quit_call():
                return

            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                swapped = True
                update_visual_callback(arr,j+1,comparisons)
        if swapped == False:
            break

