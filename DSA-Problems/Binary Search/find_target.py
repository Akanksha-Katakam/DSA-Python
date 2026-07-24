def find_target(arr,target):
    left=0
    right=len(arr)-1
    while(left<=right):
        mid=(left+right)//2
        if arr[mid]==target:
            return "Element Found"
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return "Element Not Found"
arr=list(map(int,input().split()))
target=int(input())
print(find_target(arr,target))
        