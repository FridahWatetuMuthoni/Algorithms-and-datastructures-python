def merge_sort(list):
    """ 
    The function sorts a list in ascending order
    Returns a new sorted list
    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    """
    # stopping condition for the recursion
    if (len(list) <= 1):
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    print(f"left_half: {left_half}, right_half: {right_half}")

    return merge(left, right)


def split(list):
    """ 
    Divides the unsorted list at midpoint into sublist
    Returns two sublists- left and right
    """
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    return left, right


def merge(left, right):
    """ 
    The function merges two list(arrays), and sorts them in the process
    Returns a new merged list
    """
    new_list = []
    i = 0  # for indexes in the left list
    j = 0  # for indexes in the right list

    while (i < len(left) and j < len(right)):
        if (left[i] < right[j]):
            new_list.append(left[i])
            i += 1
        else:
            new_list.append(right[j])
            j += 1

    while (i < len(left)):
        new_list.append(left[i])
        i += 1

    while j < len(right):
        new_list.append(right[j])
        j += 1

    return new_list


def verify_sorted(list):
    n = len(list)

    if (n == 0 or n == 1):
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


alist = [54, 62, 93, 17, 77, 31, 44, 55, 20]
l = merge_sort(alist)
print(l)
print(verify_sorted(l))
