#python约瑟夫环实例
def kill_person(headcount,part):
    i=2;j=0
    while True:
        j=(j+part)%i
        i+=1
        if i > headcount:
            break
    return j+1

if __name__ == '__main__':
    headcount=int(input ('please input headcound: '))
    part=int(input ('please input the part : '))
    win=kill_person (headcount,part)
    print("The number of the winner is NO.%d"%win)