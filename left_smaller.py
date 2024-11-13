from typing import List

def left_smaller(nums: List):
    result = []
    stack = []

    for num in nums:
        while stack and stack[-1] >= num:
            stack.pop()

        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)
        stack.append(num)

    return result

if __name__ == '__main__':
    nums = [5, 2, 6, 1]
    print(left_smaller(nums))
