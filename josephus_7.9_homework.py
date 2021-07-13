#约瑟夫环实例  
# 1、从三种不同的文件来创建列表。csv文件、excel文件、zip文件 2、用reader继承结构的方式，做约瑟夫环 3、用for完成约瑟夫环容器的遍历
import zipfile
import xlrd
import csv
TOTAL=15;STEP=3
__metaclass__=type
#定义student类，用于存放学生的学号、性别、姓名
class student:
    def __init__ (self,name,gender,id):
        self.name=name
        self.gender=gender
        self.id=id

#定义reader类，并调用excel,csv,zip文件中的学生信息
class reader:
    def __init__ (self,path):
        self.path=path
        
    def get_data(self):
        pass

class excel_reader(reader):
    def __init__ (self,path):
        self.path=path
        
    def get_data(self):
        global TOTAL                                       #在函数中定义全局变量TOTAL
        workbook=xlrd.open_workbook(self.path)             #打开路径下的excel文件
        sheet=workbook.sheet_by_index(0)                   #打开工作表

        student_data=[];name=[];gender=[];id=[]
        for i in range(TOTAL):                             #将工作表的信息依次放入student类中
            id.append(sheet.cell_value(i,0))               #将工作表中(i,0)单元格信息存入id列表
            gender.append(sheet.cell_value(i,1))           #将工作表中(i,1)单元格信息存入gender列表
            name.append(sheet.cell_value(i,2))             #将工作表中(i,2)单元格信息存入name列表
            student_data.append(student(id,gender,name))

            student_data[i].id=id[i]
            student_data[i].gender=gender[i]
            student_data[i].name=name[i]
        return student_data

class csv_reader(reader):
    def __init__ (self,path):
        self.path=path

    def get_data(self):
        global TOTAL
        csv_data= open(self.path,'r',encoding='utf-8')      #打开路径下的csv文件
        csv_reader=csv.reader(csv_data)                     #读取csv文件

        rows_data=[]                                        #将文件按行存入列表
        for row in csv_reader:
            rows_data.append(row)

        student_data=[];name=[];gender=[];id=[]
        for i in range(TOTAL):
            id.append(rows_data[i][0])
            gender.append(rows_data[i][1])
            name.append(rows_data[i][2])
            student_data.append(student(id,gender,name))

            student_data[i].id=id[i]
            student_data[i].gender=gender[i]
            student_data[i].name=name[i]
        return student_data
        
class zip_reader(reader):
    def __init__ (self,path):
        self.path=path

    def get_data(self):
        global TOTAL
        zip_data=zipfile.ZipFile(self.path,'r')              #调用ZipFile类
        for file_path in zip_data.namelist():                
            zip_data.extract(file_path)                      #解压目录下的文件
            sheet=adjust_document_type(file_path)
        return sheet
        

#实现约瑟夫环
def josephu_circle(student_list,start_point):
    global STEP                                              #在函数中定义全局变量STEP
    out_list=[]
    rest=list(range(1,len(student_list)+1))                  #定义rest为1~总学生数的列表
    start_point=rest.index(start_point)                      #确定查询起始位置的索引 
    
    for i in range(len(student_list)):
        out=(start_point + STEP -1)%len(rest)                #确定出局学生的列表序号
        pop_list=student_list.pop(out)
        out_list.append(pop_list)
        rest.pop(out)                                        #去除出局学生的列表序号
        start_point=out
    return out_list

#判断文件类型
def adjust_document_type(path):
    global TOTAL
    if path.endswith('.xlsx'):
        data=excel_reader(path)
        student_data=data.get_data()
    elif path.endswith('.csv'):
        data=csv_reader(path)
        student_data=data.get_data()
    elif path.endswith('.zip'):
        data=zip_reader(path)
        student_data=data.get_data()
    return student_data


if __name__ == '__main__':
    path='student_information.xlsx'
    start_point=2
    student_list=adjust_document_type(path)
    out_list=josephu_circle(student_list,start_point)

    count_student_times=0                #用来记录student出现的次数
    for student in out_list:
        count_student_times+=1
        if count_student_times<TOTAL:
            print("约瑟夫环中出局的学生是：%s %s %s"%(student.id,student.gender,student.name))
        else:
            print("约瑟夫环中胜利的学生是：%s %s %s"%(student.id,student.gender,student.name))
        


'''
调试结果如下：
约瑟夫环中出局的学生是：202104 女 赵晗
约瑟夫环中出局的学生是：202107 男 王尔佳
约瑟夫环中出局的学生是：202110 男 田毅  
约瑟夫环中出局的学生是：202113 女 赵瑟芬
约瑟夫环中出局的学生是：202101 男 王蒙
约瑟夫环中出局的学生是：202105 男 郭靖
约瑟夫环中出局的学生是：202109 女 郭晓梅
约瑟夫环中出局的学生是：202114 男 林诺
约瑟夫环中出局的学生是：202103 女 张馨然
约瑟夫环中出局的学生是：202111 男 毛文志
约瑟夫环中出局的学生是：202102 女 赵思
约瑟夫环中出局的学生是：202112 男 李磊磊
约瑟夫环中出局的学生是：202108 男 房浩
约瑟夫环中出局的学生是：202115 女 于媛媛
约瑟夫环中胜利的学生是：202106 女 李悦溪
'''