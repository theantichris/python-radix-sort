def radix_sort(to_be_sorted):
    # finding the length of the largest number
    maximum_value = max(to_be_sorted)
    max_exponent = len(str(maximum_value))

    # create a copy of the list
    being_sorted = to_be_sorted[:]

    # create buckets for each digit
    digits = [[] for i in range(10)]

    # placing a number into a bucket based on LSD
    for number in being_sorted:
        number_as_a_string = str(number)
        digit = number_as_a_string[-1]
        digit = int(digit)
        digits[digit].append(number)

    # adding numbers from digits as they appear
    being_sorted = []
    for numeral in digits:
        being_sorted.extend(numeral)

    return being_sorted

print(radix_sort([100, 201, 4278]))
