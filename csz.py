#猜数字小游戏
import random
print("猜数字游戏开始")
while True:#设置无限循环
    guess_num=int(input("请输入你要猜的数字:"))
    if guess_num in range(0,100):    #这个游戏的思路设计有问题，不是先输入数字，再猜；是程序先成随机数字，再让用户猜。不需要两层while循环
        true_num=random.randint(0,100)#随机生成一个100以内的整数
        count=1#设置一个计数器
        while guess_num != true_num:    # 用条件分支，不要用两层循环，while循环用多了会慢
            if guess_num<true_num:
                new=input("你猜小了\n请重新输入:")
            else:
                new=input("你猜大了\n请重新输入:")
            guess_num=int(new)
            count+=1
        print("恭喜你！用了{}次猜对啦".format(count))
        break
    else:
        print("输入有误，请输入一个100以内的整数")
        continue#如果输入不是100以内的整数，就返回到循环的开始
