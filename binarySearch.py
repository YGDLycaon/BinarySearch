arr=[1,2,3,4,5,6,7,8,9]
def binarySearch(arr,n):
    first=0
    last=len(arr)-1
    found=False
    while n<=last and found==False:
        mid=(first+last)/2
        if n==arr[mid]:
            found=True
        else:
            if n<=mid:
                last=mid
            else:
                first=mid
    return found

def binarySearchRec(arr,n):
    if len(arr)==0:
        return False
    else:
        mid=len(arr)/2
        if n==arr[mid]:
            return True
        else:
            if n<=mid:
                return binarySearchRec(arr[:mid],n)
            else:
                return binarySearchRec(arr[mid+1:],n)


print binarySearch(arr,1)
print binarySearchRec(arr,1)
