# def fibonacci(number):
#     last = 1
#     ans = 0
#     for i in range(0, number):
#         temp = ans
#         ans = ans + last
#         last = temp
#     return ans


def fibonacci(number):
    if number <= 0:
        return 0
    if number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)


print(fibonacci(-5))