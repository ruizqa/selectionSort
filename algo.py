
def selection_sort(arr):
    for i in range(len(arr)):
        min=arr[i]
        index = i        
        for j in range(i,len(arr)):
            if arr[j] <min:
                min = arr[j]
                index = j
        arr[i], arr[index] = arr[index], arr[i]                
    return arr


arr= [2,4,5,8,10,1,15,210,3]
print(selection_sort(arr))
