print(float('30'))
print(type('abc'))#str意思为字符串型
print(type(30.0))#float表示实数型
print(type(30))#int表示整数型
m = input("长多少米？")
cm = float(m) * 100
print("答案是：" + str(cm) + "cm")
m = input("长多少米？")
cm = m * 100
print("答案是：" + cm + "cm")#错误示例
#str(数值)  将数值转换为字符串型数据
#float(字符串)    将字符串转换为实数型数据
#int(字符串)   将字符串转换为整数型数据