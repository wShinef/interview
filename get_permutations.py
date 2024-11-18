"""
输出给定字符串的全部排列
"""

def get_permutations(s: str):
    if len(s) == 0:
        return
    if len(s) == 1:
        return [s]

    result = []
    for i in range(len(s)):
        c = s[i]
        ros = s[:i] + s[i+1:]

        for p in get_permutations(ros):
            result.append(c+p)

    return result


if __name__ == '__main__':
    str1 = 'abcd'
    print(get_permutations(str1))
