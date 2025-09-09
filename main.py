# WeightConvert.py
WeightStr = input("请输入带有符号的重量值：")
if WeightStr[-2:] == 'kg':
    # 输入的是千克，转换为磅
    lb = eval(WeightStr[0:-2]) * 2.2046
    print("转换后的重量是{:.3f}lb".format(lb))
elif WeightStr[-2:]
