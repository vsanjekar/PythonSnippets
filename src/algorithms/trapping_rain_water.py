# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#
# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
# https://leetcode.com/problems/trapping-rain-water/

def trap_rain_water(arr):
    stack = []
    index = 0;
    total_water = 0;
    while index < len(arr):
        # print stack
        bar_length = arr[index]
        # if the bar gieght is decreasing then keep going
        if not stack or bar_length <= arr[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            # bar length has increased
            # bar_length > arr[stack[-1]]:
            # pop the elements with height equal to or less than bar_length
            # while (arr[stack[-1]] <= bar_length):
            bottom_index = stack.pop()
            if not stack:
                # no left
                water = 0
            else:
                left_index = stack[-1]
                water = (min(arr[left_index],arr[index])-arr[bottom_index])*(index - left_index - 1)
            # water = 0 if (not stack) else (min(arr[stack[-1]],arr[index])-arr[bottom_index])*(index - stack[-1] - 1)
            total_water += water
    return total_water

arr = [0,1,0,2,1,0,1,3,2,1,2,1]
print trap_rain_water(arr)
arr = [3, 2, 1, 0, 0, 2, 1, 0, 4]
print trap_rain_water(arr)
