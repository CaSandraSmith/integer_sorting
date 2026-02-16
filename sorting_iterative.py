#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    O(n) if the list is sorted because we'll have to loop over the entire list
    TODO: Memory usage: ??? Why and under what conditions?
    O(1) always as there is no additional space created in this function
    """
    # TODO: Check that all adjacent items are in order, return early if so
    for idx in range(1, len(items)):
        prev = items[idx - 1]
        current = items[idx]
        if current < prev: return False
    
    return True
        

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    O(n^2) if we have to resort every item in the input array
    TODO: Memory usage: ??? Why and under what conditions?
    O(1) always as there is no additional space created in this function
    """
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    while True:
        swapped = False
        
        for idx in range(len(items) - 1):
            current = items[idx]
            next = items[idx + 1]
            
            if current > next:
                items[idx + 1] = current
                items[idx] = next
                swapped = True
        
        if not swapped: break
        
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    O(n^2) always because we always have to loop over each index of the array n times
    TODO: Memory usage: ??? Why and under what conditions?
    O(1) always as there is no additional space created in this function
    """
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    
    for idx in range(len(items)):
        current_min_idx = idx
        for idx2 in range(idx + 1, len(items)):
            if items[idx2] < items[current_min_idx]:
                current_min_idx = idx2
        
        min = items[current_min_idx]
        items[current_min_idx] = items[idx]
        items[idx] = min
    
    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    O(n^2) always because we always have to loop over each index of the array n times
    TODO: Memory usage: ??? Why and under what conditions?
    O(1) always as there is no additional space created in this function
    """
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    
    for idx in range(1, len(items)):
        inserting_item = items[idx]
        for idx2 in range(0, idx):
            current_sorted_item = items[idx2]
            if inserting_item < current_sorted_item:
                items[idx2] = inserting_item
                inserting_item = current_sorted_item
        items[idx] = inserting_item
    return items