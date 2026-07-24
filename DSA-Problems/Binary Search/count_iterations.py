def find_target(arr,target):
    left=0
    right=len(arr)-1
    count=0
    while(left<=right):
        count+=1
        mid=(left+right)//2
        if arr[mid]==target:
            break
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return count
arr=list(map(int,input().split()))
target=int(input())
print("Number of iterations : " ,find_target(arr,target))
        