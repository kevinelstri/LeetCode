import platform
print('系统:',platform.system())
 
import time
T1 = time.perf_counter()
 
#______假设下面是程序部分______
for i in range(100*100):
    pass
 
T2 =time.perf_counter()
print('程序运行时间:%s毫秒' % ((T2 - T1)*1000))
# 系统: Windows
# 程序运行时间:0.3007180604248629毫秒

'''
time 模块：
    time() 精度上较低，适合表示日期时间或者大程序程序的计时。
    
    perf_counter() 适合小一点的程序测试，会计算sleep()时间。
    
    process_counter() 适合小一点的程序测试，不会计算sleep()时间。

    此外Python3.7开始还提供了以上三个方法精确到纳秒的计时。分别是：
    time.perf_counter_ns()
    time.process_time_ns()
    time.time_ns()
    注意这三个精确到纳秒的方法返回的是整数类型。
    
    注意：clock()方法 已在Python3.8中废除
'''