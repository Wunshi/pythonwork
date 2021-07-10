#约瑟夫环实例：将容器list作为输入，容器中每个元素都是个对象，基础属性包括姓名、学号。输入要包括间隔、起始位置

#定义一个类，对象中包含的属性为学号、性别、姓名
__metaclass__=type
class person:
    def __init__ (self,name,gender,id):
        self.name=name
        self.gender=gender
        self.id=id

#录入学生的基本属性信息
def get_student_information(total):
    student_list=[]
    for i in range(total):
        student_id=input('请输入学生NO.%d的学号:'%(i+1))
        student_gender=input('请输入学生NO.%d的性别:'%(i+1))
        student_name=input('请输入学生NO.%d的姓名:'%(i+1))
        student_information=person(student_id,student_gender,student_name)
        student_list.append(student_information)
    return student_list

#实现约瑟夫环
def josephu_circle(student_list,step,start_point):
    out_list=[]
    rest=list(range(1,len(student_list)+1))       #定义rest为1~总学生数的列表
    start_point=rest.index(start_point)           #确定查询起始位置的索引 
    
    for i in range(len(student_list)):
        out=(start_point + step -1)%len(rest)     #确定出局学生的列表序号
        pop_list=student_list.pop(out)
        out_list.append(pop_list)
        rest.pop(out)                             #去除出局学生的列表序号
        start_point=out
    return out_list

#检查输入值是否为正整数
def check_for_positive_integers(num):
    if num>0:
        return num
    while num<=0:
        num=int(input('请重新输入正整数:'))
        if num>0:
            return num


if __name__ == '__main__':
    total=int(input('请输入参加约瑟夫环游戏的总人数:'))
    total=check_for_positive_integers(total)

    step=int(input('请输入step的数值:'))
    step=check_for_positive_integers(step)

    start_point=int(input('请输入从第几个学生开始该游戏:'))
    start_point=check_for_positive_integers(start_point)

    student_list=get_student_information(total)
    out_list=josephu_circle(student_list,step,start_point)

    count_student_times=0                #用来记录student出现的次数
    for student in out_list:
        count_student_times+=1
        if count_student_times<total:
            print("约瑟夫环中出局的学生是：%s %s %s"%(student.name,student.gender,student.id))
        else:
            print("约瑟夫环中胜利的学生是：%s %s %s"%(student.name,student.gender,student.id))
        

#调试结果如下
'''
请输入参加约瑟夫环游戏的总人数:9
请输入step的数值:-8
请重新输入正整数:2
请输入从第几个学生开始该游戏:0
请重新输入正整数:4
请输入学生NO.1的学号:202101
请输入学生NO.1的性别:男
请输入学生NO.1的姓名:翟天浩
请输入学生NO.2的学号:202102
请输入学生NO.2的性别:男
请输入学生NO.2的姓名:赵涵
请输入学生NO.3的学号:202103
请输入学生NO.3的性别:女
请输入学生NO.3的姓名:王冰
请输入学生NO.4的学号:202104
请输入学生NO.4的性别:男
请输入学生NO.4的姓名:哈尔
请输入学生NO.5的学号:202105
请输入学生NO.5的性别:女
请输入学生NO.5的姓名:林宛儿
请输入学生NO.6的学号:202106
请输入学生NO.6的性别:男
请输入学生NO.6的姓名:王尔佳
请输入学生NO.7的学号:202107
请输入学生NO.7的性别:女
请输入学生NO.7的姓名:郭晓梅
请输入学生NO.8的学号:202108
请输入学生NO.8的性别:女
请输入学生NO.8的姓名:赵瑟芬
请输入学生NO.9的学号:202109
请输入学生NO.9的性别:男
请输入学生NO.9的姓名:毛文志
约瑟夫环中出局的学生是：202105 女 林宛儿
约瑟夫环中出局的学生是：202107 女 郭晓梅
约瑟夫环中出局的学生是：202109 男 毛文志
约瑟夫环中出局的学生是：202102 男 赵涵
约瑟夫环中出局的学生是：202104 男 哈尔
约瑟夫环中出局的学生是：202108 女 赵瑟芬
约瑟夫环中出局的学生是：202103 女 王冰
约瑟夫环中出局的学生是：202101 男 翟天浩
约瑟夫环中胜利的学生是：202106 男 王尔佳
'''