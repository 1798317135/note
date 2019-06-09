# input("提示文字") 输出全部为字符串

content = input("请输入内容： ");
print(content,type(content));

# # 可以通过 eval()方法把输入的内容 转换为代码串
result = eval(content);
print(result,type(result));