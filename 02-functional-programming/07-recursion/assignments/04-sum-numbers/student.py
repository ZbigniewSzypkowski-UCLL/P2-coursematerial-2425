def sum_numbers(number):
    num = str(number)
    try:
        begin = int(num[0])
        if len(num) <= 1:
            return number
        else:
            return int(num[0]) + sum_numbers(int(num[1:]))
    except:
        if len(num) == 1:
            return 0
        else:
            return sum_numbers(num[1:])


print(sum_numbers(234))
print(sum_numbers(-153))