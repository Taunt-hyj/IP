import pymysql
from dbconfig import dbconfig

class db_Connect:
    #创建数据库
    flag = 0
    def __init__(self):
        try:
            self.db = pymysql.Connect(
                host=dbconfig['host'],
                user=dbconfig['user'],
                passwd=dbconfig['passwd'],
                db=dbconfig['db'],
                charset=dbconfig['charset'],
            )
        except BaseException as err:
            self.flag = 1
            print("数据库连接失败！")
            print(err)

    #关闭数据库
    def db_Close(self):
        self.db.close()

    def db_Create(self):
        sql = """CREATE TABLE IF NOT EXISTS `IP_num`(
                   `Data` char(255),
                   `num` int,
                   PRIMARY KEY ( `Data` )
                 )"""
        self.cursor.execute(sql)

    def db_Insert(self,sql,Time):
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql,(Time))
            self.db.commit()
        except:
            # 发生错误时回滚
            self.flag = 1
            self.db.rollback()
            print("数据库插入失败！")
        finally:
            self.cursor.close()

    def db_Updata(self,sql,Time):
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql,(Time))
            self.db.commit()
        except:
            # 发生错误时回滚
            self.flag = 1
            self.db.rollback()
            print('Error: unable to Updata data')
        finally:
            self.cursor.close()

    def db_Query(self,sql,Time):
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql,(Time))  # 返回 查询数据 条数 可以根据 返回值 判定处理结果
            num = self.cursor.rowcount
            if num == 0:
                sql = "INSERT INTO IP_num(Data,num) VALUES (%s, 0)"
                self.db_Insert(sql,Time)
                return 0
            else:
                data = self.cursor.fetchall()  # 返回所有记录列表
                for row in data:
                    return row[1]
        except BaseException as err:
            print(err)
            self.flag = 1
            print('Error: unable to Query data')
        finally:
            self.cursor.close()

def config_ADD(Time):
    # 连接数据库
    db = db_Connect()
    # 查询数据
    sql = "SELECT * FROM IP_num WHERE Data = %s"
    db.db_Query(sql,Time)
    # 更新数据
    sql = "UPDATE IP_num SET num=num+1 WHERE Data = %s"
    db.db_Updata(sql,Time)
    #关闭数据库
    db.db_Close()
    if db.flag == 0:
        return True
    else:
        return False

def config_QUERY(Time):
    # 连接数据库
    db = db_Connect()
    # 查询数据
    sql = "SELECT * FROM IP_num WHERE Data = %s"
    num = db.db_Query(sql,Time)
    #关闭数据库
    db.db_Close()
    if db.flag == 0:
        return {'status': 0, 'msg': "", 'num': num}
    else:
        return {'status': -1, 'msg': "操作数据库失败"}



