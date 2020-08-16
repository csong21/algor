
def merge(left, right):
    i = 0
    j = 0
    res = []
    len_left = len(left)
    len_right = len(right)

    while(i < len_left and j< len_right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    for k in range(i, len_left):
        res.append(left[k])
    for k in range(j, len_right):
        res.append(right[k])

    return res

def MergeSort(arr):

    n = len(arr)

    if n == 1:
        return arr
    else:
        m = n // 2 # floor division
        left = arr[: m]
        right = arr[m: ]
        left = MergeSort(left) 
        right = MergeSort(right)
        return merge(left, right)



if __name__ == '__main__':
    # Input list 
    a = [12, 11, 13, 7, 6, 5, 18] 
    print("Given array is") 
    print(*a) 
    print(a)

    a = MergeSort(a) 
  
    # Print output 
    print("Sorted array is : ") 
    print(*a)


  
