def radix_sort(to_be_sorted):
    # finding the length of the largest number
    maximum_value = max(to_be_sorted)
    max_exponent = len(str(maximum_value))

    # create a copy of the list
    being_sorted = to_be_sorted[:]

    # create buckets for each digit
    digits = [[] for digit in range(10)]

    return digits

print(radix_sort([1]))
