def remove_duplicates(arr):
    result = [arr[0]]
    for i in arr[1:]:
       found = False
       for j in result:
           if i==j:
               found=True
               break
       if not found:
            result.append(i)
    return result
arr=list(map(int,input().split()))
print(remove_duplicates(arr))