count = 0
nums_result = [int(i) for i in nums]
    result_digit = sum(nums_result) // len(nums_result)
    for item in nums_result:
        if item < result_digit:
            count += (result_digit - item)
        elif item > result_digit:
            count += item - result_digit
        else:
            pass
    print(count)
