def reverse(num):
    num_string = str(num)
    num_list = list(num_string)
    num_list_reverse = num_list[::-1]
    return int("".join(num_list_reverse))


print(reverse(123456789))
