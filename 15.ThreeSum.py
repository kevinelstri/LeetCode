'''
    给定一个数组，找出数组中三个元素之和等于0的列表
    input：[-1, 0, 1, 2, -1, 2, -4]
    output:[[-1, 0, 1],
            [-1, -1, 2],
            [2, 2, -4]]
'''

from typing import Counter

# 先排序，再顺序遍历，出现重复结果（原因：无法减少元素个数，导致元素被重复使用，产生重复结果）
def threeSum(nums, target):
    hash_dic = sorted(nums)

    in_result = []
    for index, a in enumerate(hash_dic):
        print(hash_dic[index:])
        print('index:'+str(index))
        for next, b in enumerate(hash_dic[index+1:]):
            next = next + index + 1
            if a + b >= target:
                continue
            if a == b:
                index = index + 1
            c = target - (a + b)
            print('next:'+str(next))
            if c in hash_dic[next+1:]:
                third = next + hash_dic[next+1:].index(c) + 1
                print('third:'+str(third))
            if (c in hash_dic[next+1:] and b != c) or \
               (c in hash_dic[next+1:] and b == c and third > next) or \
               (c in hash_dic[next+1:] and a == c and third > index):
                in_result.append([a, b, c])
                print([a, b, c])
        print('-------------------------------------------------------')
    return in_result

# 哈希表方法，避免重复结果
def threeSum2(nums, target):
    dic = Counter(nums)
    hash_dic = sorted(dic.keys())
    print(hash_dic)
    print(dic)
    in_result = []

    for index, a in enumerate(hash_dic):
        print(dic)
        dic[a] -= 1  # 字典中已经使用一个，就减少一个
        for b in hash_dic[index:]:
            if dic[b] < 1:  # 通过字典来判断元素个数，元素为0，就不再计算
                continue
            c = target - (a + b)
            if c < b:
                break
            if (c > b and dic[c] > 0) or (c == b and dic[c] > 1):
                in_result.append([a, b, c])
    return in_result


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, 2, -4, 5, 9]
    target = 0
    resultSet = threeSum(nums, target)
    print(resultSet)
    print('------------------------------------------')
    resultSet2 = threeSum2(nums, target)
    print(resultSet2)
