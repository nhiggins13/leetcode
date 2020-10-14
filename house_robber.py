def rob(house_list):

    prevMax = 0
    currMax = 0

    for num in house_list:
        temp = currMax
        currMax = max(prevMax + num, currMax)
        prevMax = temp

    return currMax


h_list = [3, 1, 2, 5, 4, 2]

print(rob(h_list))

print(h_list[0:-1])