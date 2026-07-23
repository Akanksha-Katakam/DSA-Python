def second_lar_element(arr):
    largest=arr[0]
    second=float('-inf')
    for i in range(len(arr)):
        if arr[i]>largest:
            second=largest
            largest=arr[i]
        elif arr[i]>second and arr[i]!=largest:
            second=arr[i]
    return second
arr=list(map(int,input().split()))
sec = second_lar_element(arr)
print("second Largest Element is: ",sec)
