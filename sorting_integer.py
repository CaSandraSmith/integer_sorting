#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: O(n + m), where m is the range of elements in the input list,
    and n is the size of the input array, always because we have to loop over each 
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
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    minimum = min(numbers)
    maximum = max(numbers)
    range = maximum - minimum + 1
    
    # TODO: Create list of buckets to store numbers in subranges of input range
    buckets = []
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list