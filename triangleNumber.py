from typing import List
"""
双指针返回有效的三角形个数
"""
def triangleNumber(nums: List):
    nums.sort()
    count = 0
    for k in range(2, len(nums)):
        i, j = 0, k-1
        while i < j:
            if  nums[i] + nums[j] > nums[k]:
                count += j - i
                j -= 1

            else:
                i += 1

    return count

if __name__ == '__main__':
    nums = [2, 2, 3, 4]
    print(triangleNumber(nums))
