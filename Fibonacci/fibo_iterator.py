#-*-    coding:utf-8    -*-
'''
用迭代器实现斐波那契前n项数列
'''
class Fibonacci():    #创建类来实现迭代  ## 去掉括号

    def __init__(self,n):    #进行初始化    
        self.n = n    #n是数列生成的个数
        self.value = 0    #当前生成的第几个数据，用于与下一个位置的值比较   ## 这个属性可以去掉
        self.num1 = 0
        self.num2 = 1

            
    def __iter__(self):
        return self

    def __next__(self):   #每调用一次next()函数，就会获取一个值
        if self.value == 0:
            self.num1, self.num2 = self.num1 , self.num2
        elif self.value<self.n: 
            self.num1, self.num2 = self.num2 , self.num1 + self.num2
            '''从第三项开始，每一项都是前两项的和'''
        else:    #超过则停止
            raise StopIteration
        self.value += 1
        return self.num1

if __name__=='__main__':
    while True:
        terms=input("请输入项数：")    
        if not terms.isdigit():    #判断输入是否符合要求
            print("输入有误，请输入一位正整数")
        else:
            n=int(terms)    
            print(f'斐波那契前{n}项数列为:') 
            for i in Fibonacci(n):
                print(i,end=' ')
            break

