def InsertionSort(arr,n):
    for i in range(1,n):
        val=arr[i]
        hole=i
        while hole>0 and arr[hole-1]>val:
            arr[hole]=arr[hole-1]
            hole=hole-1
        arr[hole]=val
arr=[7,2,4,1,5,3]
InsertionSort(arr,len(arr))
print(arr)