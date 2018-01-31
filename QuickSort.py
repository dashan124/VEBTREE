def partition(arr,start,end):
    pivot=arr[end]
    pindex=start
    for i in range(start,end-1):
        if arr[i]<=pivot:
            temp=arr[i]
            arr[i]=arr[pindex]
            arr[pindex]=temp
            pindex=pindex+1
    t=arr[pindex]
    arr[pindex]=arr[end]
    arr[end]=t
    return pindex
def QuickSort(arr,start,end):
    if start<end:
        pi=partition(arr,start,end)
        print(pi)
        QuickSort(arr,start,pi-1)
        QuickSort(arr,pi+1,end)
arr=[7,2,1,6,8,5,3,4]
QuickSort(arr,0,len(arr)-1)
print(arr)