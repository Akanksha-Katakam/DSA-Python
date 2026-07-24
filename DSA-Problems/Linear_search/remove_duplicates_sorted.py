def remove_duplicates(arr):
    result=[arr[0]]
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            result.append(arr[i])
    return result
arr=list(map(int,input().split()))
print(remove_duplicates(arr))
            