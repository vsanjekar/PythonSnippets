def maximum_subarray_sum(arr):
    max_so_far = 0
    max_ending_here = 0
    for x in arr:
        max_ending_here = max(x, max_ending_here+x)
        max_so_far = max(max_ending_here, max_so_far)
    return max_so_far

arr = [1, 4, -5 , 100, -1000, 5, 50, -10, 100]
print maximum_subarray_sum(arr)
