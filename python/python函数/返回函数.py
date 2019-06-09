

# ------------ 函数内部可以往外部返回函数体 然后把函数体赋值给变量
# 
def getFun(flag):
    
    # 1.0 定义函数
    def jia(a,b,c):
        return a + b + c

    def jian(a,b,c):
        return a - b - c

    # 2.0 判定
    if flag == "+":
        return jia
    elif flag == "-":
        return jian

result = getFun("-")
print(result(1,2,3))
        