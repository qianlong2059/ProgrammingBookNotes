#=================================== 创建Python类 ===================================#
class MyFirstClass:
    pass

# 类定义以 class 关键字开始，接着是类的名字，然后是冒号
# 类名必须遵循标准的Python变量名准则（必须以字母或下画线开头，并只能由字母、下画线或数字组成），建议类名应该用驼峰格式命名

a = MyFirstClass()  # 创建类的实例
print(a)    
# <__main__.MyFirstClass object at 0x000001EF46F2D9D0> 输出的是类对象以及他们被存储的内存地址


#=================================== 添加类的属性 ===================================#
class Point():
    pass

p1 = Point()
p2 = Point()

p1.x = 1
p1.y = 2

p2.x = 3
p2.y = 4

print(p1.x, p1.y,p2.x, p2.y)  # 1 2 3 4
    # 点对象法，赋值语法为 <对象>.<属性>=<值>
    # <值>可以是任何类型: Python的基本类型，内置数据类型或者其他的对象，甚至可以是一个函数或另一个类


#=================================== 添加类的方法 ===================================#
class Reset():
    def reset(self):    # 类的方法在格式上与函数完全一致，以def关键字开头，紧接着的是一个空格和方法名，然后是一对括号括起来的参数列表
        self.x = 0      # 下一行是包含方法内部语句的代码块
        self.y = 0

r = Reset()
r.x = 5
r.y = 6
print(r.x, r.y)  # 5 6

r.reset()
print(r.x, r.y)  # 0 0
        
#=================================== 初始化对象 ===================================#
# 在Python中，类的方法可以有一个特殊的名称：__init__。当创建类的实例时，Python会自动调用这个方法。这个方法通常用于初始化对象的属性。
class MovePoint():
    def __init__(self,x,y):
        self.move(x,y)
        
    def move(self,x,y):
        self.x = x
        self.y = y
    
    def reset(self):
        self.move(0,0)

point = MovePoint(1,2)
print(point.x, point.y)  # 1 2

#=================================== 数据访问 ===================================#
# 严格来说，类的所有方法和属性都是对外公开的