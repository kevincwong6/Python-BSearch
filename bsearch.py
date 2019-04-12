def bsearch(arr, val):
    start=0
    last=len(arr)-1
    mid=last//2

    while(last >= start):
        if arr[mid]==val:
            return mid
        elif arr[mid] > val:
            last = mid - 1
        else:
            start = mid + 1

        mid = (start+last)//2

    return -1

arr=[1,2,3,4,5,6,7]
rc=bsearch(arr, 7)

if (rc == -1):
    print("BSearch not able find a matched value.")
else:
    print("BSearch matched value at index "+str(rc))

######################
# Output
# BSearch matched value at index 6
#
