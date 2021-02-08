def reverse_integer(nums):
    reversed1 = 0
    remainder = 0

    while nums > 0:
        remainder = nums % 10
        nums = nums // 10
        reversed1 = reversed1 * 10 + remainder
    
    return reversed1

print(reverse_integer(1234))