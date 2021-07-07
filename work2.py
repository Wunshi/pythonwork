# %%
import pymysql
import random
ALPHA="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
ALPHA_LENGTH=len(ALPHA)-1
NUM=200
def promote_codes (length):
    code=[]
    for j in range(length):
        n=random.randint(0,ALPHA_LENGTH)
        code.append(ALPHA[n])
    code="".join(code)
    return code

def create_database():
    db=pymysql.connect(host='localhost',user='root',password='Long',port=3306)
    #建立游标
    cursor=db.cursor()
    #建立数据库
    cursor.execute('create database pyth DEFAULT CHARACTER SET utf8mb4')
    db.close()
    return db

def create_table():
    db=pymysql.connect(host='localhost',user='root',password='Long',port=3306,db='pyth')
    #建立游标
    cursor=db.cursor()
    #建立数据库
    cursor.execute('create table if not exists work(id VARCHAR(255) NOT NULL, code VARCHAR(255) NOT NULL, PRIMARY KEY (id))')
    db.close()
    return db

def generate_table_insert(i,codes):
    db=pymysql.connect(host='localhost',user='root',password='Long',port=3306,db='pyth')
    cursor=db.cursor()
    data={
        'id':'NO.%d'%i,
        'code':'%s'%codes
    }
    table='work'
    keys=','.join(data.keys())
    values=','.join(['%s']*len(data))
    sql='insert into {table}({keys}) VALUES({values})'.format(table=table,keys=keys,values=values)
    try:
        if cursor.execute(sql,tuple(data.values())):
            print('insert successful')
            db.commit()
    except Exception as e:
        print("insert failed!",e)
        db.rollback()
    db.close()
    return db

if __name__ =='__main__':
    create_database()
    create_table()
    for i in range(NUM):
        codes=promote_codes (5)
        generate_table_insert(i,codes)

