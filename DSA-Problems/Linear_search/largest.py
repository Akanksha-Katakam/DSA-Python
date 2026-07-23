def lar_element(arr):
    largest=arr[0]
    index=0
    for i in range(len(arr)):
        if arr[i]>largest:
            largest=arr[i]
            index=i
    return largest,index
arr=list(map(int,input().split()))
lar,idx = lar_element(arr)
print("Largest Element is: ",lar)
print("Index: ", idx)