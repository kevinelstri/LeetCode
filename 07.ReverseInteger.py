'''
    逆序输出给定整形数字，注意是数字，不是字符串
    input: 123  -234  120
    output:321  -432  21
'''

# 数学方法
def reverseInteger(num):
    numx = 0
    if num < 0:
        numx = abs(num)
    else:
        numx = num

    tmp = ''
    while numx//10 != 0:
        tmp += str(numx%10)
        numx = numx//10
    tmp += str(numx)
    
    if num < 0:
        tmp = '-' + tmp

    return int(tmp)


if __name__ == '__main__':
    num = -1230
    reNum = reverseInteger(num)
    print(reNum)
