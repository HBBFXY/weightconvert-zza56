# WeightConvert,py
weight_str=input("请输入带有符号的重量值")
if WeightStr[-2:].lower()=='kg';
1b=eval(WeightStr[0:-2])*2.2046
print("转换后的重量是{：4f}1b".format(1b))
elif WeightStr[-2:].lower()=='1b':
kg=eval(WeightStr[0:-2])/2.2046
print("转换后的重量是{:.4f}kg".format(kg))
else:
print("输入格式错误，请使用'kg'表示千克或'1b'表示磅")
