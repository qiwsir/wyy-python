# -*- coding: utf-8 -*-
'''将阿拉伯数字转换为罗马数字'''

class Roman:
    def __init__(self,num):
        self.num=num
     
    def A_exchange_R(self): 
        convert={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
        result = []
        for i in convert:     #将想要转换的数字从列表中最大的开始比到最小的
            while self.num >= i:    ## 避免使用for里面嵌套while的写法。
                result.append(convert[i])
                self.num -= i
        return result   

a = Roman(39999)
result = a.A_exchange_R()
print(''.join(result))
