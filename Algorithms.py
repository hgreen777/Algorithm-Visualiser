
def bubbleSort(arr, update_visual_callback, quit_call):
    n = len(arr) 

    for i in range(n):
        swapped = False
        for j in range (0, n-i-1):
            if quit_call():
                return


            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                swapped = True
                update_visual_callback(arr,j+1)
        if swapped == False:
            break

