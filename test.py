def operation_with_arguments(arg1, arg2):

    # try:
    #     arg1 = float(arg1)
    # except ValueError:
    #     pass
    #
    # try:
    #     arg2 = float(arg2)
    # except ValueError:
    #     pass

    if isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):
        return f'multiplication {arg1 * arg2}'

    if isinstance(arg1, str) and isinstance(arg2, str):
        return f'concatenation {arg1 + arg2}'
    else:
        return f'The result is tuple: {(arg1, arg2)}'

# a = input('arg1 = ')
# b = input('arg2 = ')


print(operation_with_arguments(['qwe',123],(123, 2, 3)))