'''
    给定一个list，查找list中满足两个数字之和等于target目标数字的两个数字的索引
'''
import time

# 暴力循环法 O(n2)
def twoSum1(nums, target):
    numLen = len(nums)
    for i in range(0, numLen):
        for j in range(i+1, numLen):
            if nums[i] + nums[j] == target:
                return [i,j]

# enumerate枚举 索引序列 O(n2) 注意：此方法和暴力破解方法具有一致性，只是形式不一样
def twoSum2(nums, target):
    for a,i in enumerate(nums):
        for b,j in enumerate(nums):
            if nums[i] + nums[j] == target and a != b :
                return [i,j]

# 直接查找满足条件的两个数字的索引  O(n)
def twoSum3(nums, target):
    for firstNum in nums:
        secondNum = target - firstNum
        firstIndex = nums.index(firstNum)
        if secondNum in nums[firstIndex+1:]:
            secondIndex = nums.index(secondNum)
            return [firstIndex, secondIndex]

# 哈希表
def twoSum4(nums,target):
    dic = {}
    for index, num in enumerate(nums):
        tmp = target - num
        if tmp in dic:
            return [dic[tmp], index]  # 哈希表dic中的数据是先添加进去的，所以放到list前面
        dic[num] = index


if __name__ == '__main__':
    target = 10
    nums = [3, 4, 5, 8, 11, 2]
    startTime = time.perf_counter()
    result1 = twoSum1(nums, target)
    endTime = time.perf_counter()
    print(str(result1) + ' ' + '程序运行时间：%s毫秒' % ((endTime - startTime)*1000))

    startTime = time.perf_counter()
    result2 = twoSum2(nums, target)
    endTime = time.perf_counter()
    print(str(result2) + ' ' + '程序运行时间：%s毫秒' % ((endTime - startTime)*1000))
    
    startTime = time.perf_counter()
    result3 = twoSum3(nums, target)
    endTime = time.perf_counter()
    print(str(result3) + ' ' + '程序运行时间：%s毫秒' % ((endTime - startTime)*1000))

    startTime = time.perf_counter()
    result4 = twoSum4(nums, target)
    endTime = time.perf_counter()
    print(str(result4) + ' ' + '程序运行时间：%s毫秒' % ((endTime - startTime)*1000))

    # 注意：enumerate枚举遍历时，前面是索引，后面是元素
    for a, j in enumerate(nums):
        print(a,j)
