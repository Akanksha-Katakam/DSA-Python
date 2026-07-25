def last_duplicate(arr):
    last=-1
    value=-1
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                if j>last:
                    last=j
                    value=arr[i]
    return value,last
arr=list(map(int,input().split()))
value,last=last_duplicate(arr)
print("Last duplicate element : ",value)
print("Last duplicate index : ",last)