#given transformation = 3
#given arr of int 3
# if element of arr is even then sub it by 3 & if odd the add by 3



def oddeventransform(arr, transform):
    for i in range(transform):
        for i in range(len(arr)):
            if arr[i]%2==0:
                arr[i]= arr[i]-3
            else:
                arr[i]= arr[i]+3
    return arr

arr = [0,0,0]
transform = 3
callfun= oddeventransform(arr, transform)
print(callfun)
