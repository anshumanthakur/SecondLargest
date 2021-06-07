import sys

def printSecondLargest(arr):
    max1 = sys.maxsize - 1
    max2 = -sys.maxsize

    print(max1)

    if(len(arr) < 2):
        return ("-1")
    if(len(arr) >1024):
        return("array size exceeded")

    for i in arr:
        try:
            current = int(i)
            if(current > 2147483647):
                return("please enter smaller value")
            if(current>max1):
                max2=max1
                max1=current
            elif(current>max2 and current != max1):
                max2=current
        except ValueError:
            return("invalid Input")

    if(max2 == -sys.maxsize):
        return("-1")
    result = "Second largest element is " + str(max2)
    return (result)

arr =  []
result = printSecondLargest(arr)
print(result)

