'''
    两个排序数组的中位数
    input:num1=[1,3] num2=[2]
    output:2

    input:num1=[1,2], num2=[3,4]
    output:2.5

    思路1：数学方法，使用除法来计算中间那个数，再分别在两个数组中查找中间那个数
    思路2：两个数组合并成一个数组，直接求中间那个数
'''

# 合并两个有序数组
def mergeTwoSortedArray(list1, list2):
    firstBegin = 0
    secondBegin = 0
    mergeList = []
    firstLen = len(list1)
    secondLen = len(list2)
    while firstBegin < firstLen and secondBegin < secondLen:
        ele1 = list1[firstBegin]
        ele2 = list2[secondBegin]
        if ele1 < ele2:
            mergeList.append(ele1)
            firstBegin += 1
        elif ele1 > ele2:
            mergeList.append(ele2)
            secondBegin += 1
        else:
            mergeList.append(ele1)
            mergeList.append(ele2)
            firstBegin += 1
            secondBegin += 1
    if firstBegin < firstLen:
        mergeList.extend(list1[firstBegin:firstLen])
    if secondBegin < secondLen:
        mergeList.extend(list2[secondBegin:secondLen])
    return mergeList

# 查找中位数
def findMedianWithTwoSortedArray(mergeList):
    if len(mergeList) % 2 != 0:
        median = mergeList[len(mergeList)/2]
        return median
    else:
        median = (mergeList[len(mergeList)//2-1] + mergeList[len(mergeList)//2])/2
        return median


if __name__ == '__main__':
    list2 = [1, 2, 3, 4]
    list1 = [5, 6]
    mergeList = mergeTwoSortedArray(list1, list2)
    median = findMedianWithTwoSortedArray(mergeList)
    print(mergeList)
    print(median)
