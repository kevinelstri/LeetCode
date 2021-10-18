'''
    寻找最长无重复子串，子串中不包含重复元素
    input: 'abcabcbb'
    output: 3
    Explanation: The answer is 'abc', with the length of 3
'''

# 寻找最长无重复子串
def longestSubstring(str):
    left = 0
    right = left + 1
    strLength = len(str)
    strList = []
    maxLength = 0
    maxStr = ''
    while right <= strLength:
        strList = list(str[left:right])
        ele = str[right:right+1]
        if ele not in strList:
            right += 1
        else:
            maxTemp = right - left
            if maxLength < maxTemp:
                maxLength = maxTemp  # 获取无重复子串的长度
                maxStr = str[left:right]  # 获取最长无重复子串
            left += 1
            right = left + 1
    return maxLength,maxStr

if __name__ == '__main__':
    str = 'pwwkew'
    maxLength,maxStr = longestSubstring(str)
    print(maxLength,maxStr)