'''
    一个非负整数构成的数组，使用这个数组来按顺序构建一个柱状图，在柱状图直接注入水，求最大蓄水的柱状图面积
'''

# 双指针方法，指针分别从两端向中间移动，并计算蓄水面积
# 指针从较低的柱状图向内移动，每次只保存最大的蓄水面积，直到柱状图重合
# 时间复杂度 O(n)
def mostWater(waterList):
    first = 0
    last = len(waterList)-1
    maxWater = min(waterList[first],waterList[last])*(last-first)
    print(first, last, maxWater)
    while first != last:
        if waterList[first] < waterList[last]:
            first = first + 1
            maxTemp = min(waterList[first],waterList[last])*(last-first)
            print(first, last, maxTemp)
            maxWater = maxWater if maxWater > maxTemp else maxTemp
        else:
            last = last - 1
            maxTemp = min(waterList[first],waterList[last])*(last-first)
            print(first, last, maxTemp)
            maxWater = maxWater if maxWater > maxTemp else maxTemp
    return maxWater

def min(a,b):
    return a if a < b else b

def max(a, b):
    return a if a > b else b


if __name__ == '__main__':
    water = [1,8,6,2,5,4,8,3,7]
    maxWater = mostWater(water)
    print(maxWater)
