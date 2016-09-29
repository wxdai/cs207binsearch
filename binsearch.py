def binary_search(da_array: list, needle, left:int=0, right:int=-1) -> int:
    if left==0:
        rangemin = 0
    else:
        rangemin = left
    if right==-1:
        rangemax=len(da_array) - 1
    else:
        rangemax=right
    while True:
        "needle in da_array => needle in da_array[rangemin:rangemax]"   
        if rangemin > rangemax:
            index = -1
            return index
        #If rangemin and rangemax are both very high we do not want overflow,
        #so get the midpoint like this:
        midpoint = rangemin + (rangemax - rangemin)//2
        if da_array[midpoint] > needle:#lower part
            rangemax = midpoint - 1
        elif da_array[midpoint] < needle:
            rangemin = midpoint + 1
        else:
            index = midpoint
            return index


