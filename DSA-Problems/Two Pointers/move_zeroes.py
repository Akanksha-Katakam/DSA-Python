arr=[1,0,2,0,3,0]
left = 0
for right in range(len(arr)):
    if arr[right] != 0:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
print(arr)