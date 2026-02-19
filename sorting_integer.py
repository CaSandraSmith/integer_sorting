#!python
from sorting_recursive import merge_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: O(n + m), where m is the range of elements in the input list,
    and n is the size of the input list, always because we have to loop over each 
    element in the input list and also loop over the size of the range list
    TODO: Memory usage: O(m) where m is the range of elements in the input list, always
    """
    if len(numbers) <= 1: return numbers
    # TODO: Find range of given numbers (minimum and maximum integer values)
    minimum = min(numbers)
    maximum = max(numbers)
    
    # TODO: Create list of counts with a slot for each number in input range
    counts = [0] * (maximum - minimum + 1)

    # TODO: Loop over given numbers and increment each number's count
    for num in numbers:
        slot = num - minimum
        counts[slot] += 1
    
    # TODO: Loop over counts and append that many numbers into output list
    # output = []
    # for i in range(len(counts)):
    #     count = counts[i]
    #     output.extend([minimum + i] * count)
    # return output
    
    # FIXME: Improve this to mutate input instead of creating new output list
    count_idx = 0
    for i in range(len(numbers)):
        while counts[count_idx] == 0: 
            count_idx += 1
        numbers[i] = minimum + count_idx
        
        counts[count_idx] -= 1

    return numbers
    

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: O(n log n/m) where m is the number of buckets in the best 
    case where the items are evenly distributed over the buckets because we are are 
    able to divide the number of elements in each call of merge sort by the number of
    buckets. In the worst case where all of the elements are in one bucket, time complexity 
    is O(n log n) which would be the full merge sort cost without the efficiency provided 
    by dividing the items into buckets.
    TODO: Memory usage: O(m + n) always because we create an a new list for each bucket
    and all of the numbers are contained within the buckets
    """
    if len(numbers) <= 1: return numbers
    
    # TODO: Find range of given numbers (minimum and maximum values)
    minimum = min(numbers)
    maximum = max(numbers)
    range_count = maximum - minimum + 1
    range_per_bucket = range_count / num_buckets
    
    # TODO: Create list of buckets to store numbers in subranges of input range
    buckets = [[] for i in range(num_buckets)]

    # TODO: Loop over given numbers and place each item in appropriate bucket
    for num in numbers:
        bucket_index = int((num - minimum) / range_per_bucket)
        buckets[bucket_index].append(num)
        
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    for bucket in buckets:
        merge_sort(bucket)
    
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # output = []
    
    # for bucket in buckets:
    #     output.extend(bucket)
    
    # return output
    
    # FIXME: Improve this to mutate input instead of creating new output list
    current_num_index = 0
    for i in range(num_buckets):
        if len(buckets[i]) != 0:
            for j in range(len(buckets[i])):
                numbers[current_num_index] = buckets[i][j]
                current_num_index += 1
    
    return numbers