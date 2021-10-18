'''
    罗马数字转换成十进制数字
   
    字母  数值
    I   1
    V   5
    X   10
    L   50
    C   100
    D   500
    M   1000
'''

def romanToInteger(roman):
    romanDic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    romanList = list(roman)
    integer = 0
    for i in range(0,len(romanList)-1):
        if romanList[i] == 'I' and romanList[i+1] == 'V':
            integer += 4
            i += 2
        elif romanList[i] == 'I' and romanList[i+1] == 'X':
            integer += 9
            i += 2
        elif romanList[i] == 'X' and romanList[i+1] == 'L':
            integer += 40
            i += 2
        elif romanList[i] == 'X' and romanList[i+1] == 'C':
            integer += 90
            i += 2
        elif romanList[i] == 'C' and romanList[i+1] == 'D':
            integer += 400
            i += 2
        elif romanList[i] == 'C' and romanList[i+1] == 'M':
            integer += 900
            i += 2
        else:
            integer += romanDic[romanList[i]]
    
    if (romanList[len(romanList)-2] == 'I' and romanList[len(romanList)-1] == 'V') or (romanList[len(romanList)-2] == 'I' and romanList[len(romanList)-1] == 'X') or \
       (romanList[len(romanList)-2] == 'X' and romanList[len(romanList)-1] == 'L') or (romanList[len(romanList)-2] == 'X' and romanList[len(romanList)-1] == 'C') or \
       (romanList[len(romanList)-2] == 'C' and romanList[len(romanList)-1] == 'D') or (romanList[len(romanList)-2] == 'C' and romanList[len(romanList)-1] == 'M'):
        integer = integer
    else:
        integer += romanDic[romanList[len(romanList)-1]]

    return integer

if __name__ == '__main__':
    roman = 'MCMLXXVI'
    integer = romanToInteger(roman)
    print(integer)