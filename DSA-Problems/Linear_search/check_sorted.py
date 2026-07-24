def sorted(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True
arr=[10,20,30,40,50]
print(sorted(arr))