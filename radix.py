def radix_sort(to_be_sorted):
    max_exponent = len(str(max(to_be_sorted)))

    being_sorted = to_be_sorted[:]  # create a copy of the list

    # loop through each digit based on largest exponent
    for exponent in range(max_exponent):
        digits = [[] for i in range(10)]  # create buckets for each digit
        index = -(exponent + 1)  # get the string index for the number

        for number in being_sorted:  # placing numbers into a bucket based on LSD
            number_as_a_string = str(number)

            try:
                digit = int(number_as_a_string[index]) # getting digit at current place
            except IndexError:
                digit = 0 # if number doesn't have this digit it is 0

            digits[digit].append(number)

        # adding numbers from digits as they appear
        being_sorted = []
        for numeral in digits:
            being_sorted.extend(numeral)

    return being_sorted

my_list = [234, 3981, 1, 48276, 23]
print(my_list)
print(radix_sort(my_list))
