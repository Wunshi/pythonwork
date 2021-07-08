#约瑟夫环实例：将容器list作为输入，容器中每个元素都是个对象，基础属性包括姓名、学号。输入要包括间隔、起始位置
#实现约瑟夫环
def josephu_ring(mes,step,start):
    rest=list(range(1,len(mes)+1))
    start_point=rest.index(start)
    for i in range(len(mes)-1):
        kill=(start_point + step -1)%len(rest)
        print('该学生在游戏中死亡，他的身份信息是\n%s'%mes[kill])
        rest.pop(kill)
        mes.pop(kill)
        start_point=kill
    print('游戏中最终胜利的学生身份信息是\n%s'%mes)
    return mes

#录入学生的基本属性信息
def input_information(total):
    message_list=[]
    for i in range(total):
        message=input('请依次输入学生NO.%d的学号、性别、姓名:'%(i+1))
        message_list.append(message)
    return message_list

#检查输入值是否为正整数
def check_input(num):
    if num>0:
        return num
    while num<=0:
        num=int(input('请重新输入正整数:'))
        if num>0:
            return num

if __name__ == '__main__':
    total=int(input('请输入参加约瑟夫环游戏的总人数:'))
    total=check_input(total)
    mes=input_information(total)
    print(mes)
    step=int(input('请输入step的数值:'))
    step=check_input(step)
    start=int(input('请输入从第几个学生开始该游戏:'))
    start=check_input(start)
    josephu_ring(mes,step,start)