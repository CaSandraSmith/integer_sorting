#!python
import math

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: O(n) always because we have to loop through every item in each items list
    TODO: Memory usage: O(n) always because we're creating a new list that is the length of each items list combined"""
    p1 = 0
    p2 = 0
    merged_list = []
    
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    while p1 < len(items1) or p2 < len(items2):
        if not p1 >= len(items1) and (p2 >= len(items2) or items1[p1] < items2[p2]):
            merged_list.append(items1[p1])
            p1 += 1
        else:
            merged_list.append(items2[p2])
            p2 += 1

    return merged_list


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: O(n log n) because we're splitting the list in half on each 
    iteration and doing a linear operation inside each turn
    TODO: Memory usage: O(n) because we are creating a new list that contains all of 
    the elements from the input list and this is more complex than the O(log n) complexity
    of calls added to the call stack
    """
    # TODO: Check if list is so small it's already sorted (base case)
    if len(items) <= 1:
        return items
    
    # TODO: Split items list into approximately equal halves
    middle = math.floor(len(items) / 2)
    left = items[:middle]
    right = items[middle:]

    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    merged_list = merge(merge_sort(left), merge_sort(right))
    
    for idx in range(len(merged_list)):
        items[idx] = merged_list[idx]
        
    return items


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a middle pivot from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: O(n) if we are sorting the whole list because we have to loop over every item in the list
    TODO: Memory usage: O(1) because we aren't creating any new memory in this function"""
    # TODO: Choose a pivot any way and document your method in docstring above
    pivot = math.floor((low + high) / 2)
    pivot_value = items[pivot]
    
    items[pivot] = items[high]
    items[high] = pivot_value
    
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    for idx in range(low, high):
        current_item = items[idx]
        
        if current_item < pivot_value:
            items[idx] = items[low]
            items[low] = current_item
            low += 1
    
    items[high] = items[low]
    items[low] = pivot_value
        
    # TODO: Move pivot item into final position [p] and return index p
    return low


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: O(n log n) because we're splitting the list in half on each 
    iteration and doing a linear operation inside each turn in the case that
    partitioned sections are relatively evenly split during each iteration
    TODO: Worst case running time: O(n^2) in the case that the selected pivot constantly 
    creates partitioned sections are skewed so that future iterations aren't spliting 
    the previous sections in half
    TODO: Memory usage: O(n) in the worst case that the selected pivot constantly creates 
    partitioned sections are skewed so that future iterations aren't spliting the previous 
    sections in half and so the call stack would contain one call per element in the input array.
    If the partitions are relatively evenly split then the space complexity would be O(log n)
    """
    # TODO: Check if high and low range bounds have default values (not given)
    if low == None and high == None:
        low = 0
        high = len(items) - 1
        
    # TODO: Check if list or range is so small it's already sorted (base case)
    if len(items) <= 1 or high - low <= 0:
        return items
    
    # TODO: Partition items in-place around a pivot and get index of pivot
    partition_index = partition(items, low, high)
    
    # TODO: Sort each sublist range by recursively calling quick sort
    quick_sort(items, low, partition_index - 1)
    quick_sort(items, partition_index + 1, high)
    
    return items