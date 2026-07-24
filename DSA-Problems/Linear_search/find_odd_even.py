def odd_even(arr):
    odd=[]
    even=[]
    for i in arr:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return odd,even
arr=[1,2,3,4,5,6]
odd,even=odd_even(arr)
print("Odd : " ,odd)
print("Even : " ,even)
