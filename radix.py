def radix_sort(to_be_sorted):
    # finding the number of digits of the largest number
    maximum_value = max(to_be_sorted)
    max_exponent = len(str(maximum_value))

    # create a copy of the list
    being_sorted = to_be_sorted[:]

    # loop through each digit based on largest exponent
    for exponent in range(max_exponent):
        # create buckets for each digit
        digits = [[] for i in range(10)]

        # get index for the number as a string
        position = exponent + 1
        index = -position

        # placing a number into a bucket based on LSD
        for number in being_sorted:
            number_as_a_string = str(number)

            try:
                digit = number_as_a_string[index]
            except IndexError:
                digit = 0 # if number doesn't have this digit it is 0

            digit = int(digit)
            digits[digit].append(number)

        # adding numbers from digits as they appear
        being_sorted = []
        for numeral in digits:
            being_sorted.extend(numeral)

    return being_sorted

my_list = [234, 3981, 1, 48276, 23]
print(my_list)
print(radix_sort(my_list))
