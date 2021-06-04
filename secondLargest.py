
def printSecondLargest(arr):
    max1 = -2147483648
    max2 = -2147483648

    if(len(arr) < 2 or len(arr)>1024):
        return ("invalid Input")

    for i in arr:
        current = int(i)
        if(current > 2147483647):
            return("please enter smaller value")
        try:
            if(current>max1):
                max2=max1
                max1=current
            elif(current>max2 and current != max1):
                max2=current
        except ValueError:
            return("invalid Input")
                
    result = "Second largest element is " + str(max2)
    return (result)


arr = ["8","21","6","2","1","4"]
result = printSecondLargest(arr)
print(result)

