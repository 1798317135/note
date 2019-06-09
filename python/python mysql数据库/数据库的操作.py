###############################  创建表 ################################
#
import mysql.connector
import contextlib

class cb:
    def __enter__(self):
        mydb = mysql.connector.connect(
            user = 'root',
            password = '123456',
            host = 'localhost',
            database = 'test1',
            charset = 'utf8'
        )
        self.db = mydb
        return self.db

    def __exit__(self,exc_type,exc_value,ext_tb):
        # print(self,exc_type,exc_value,ext_tb)
        import traceback
        if traceback.extract_tb(ext_tb):
            print(traceback.extract_tb(ext_tb))
            self.db.rollback()
        return True
        
with cb() as mydb:
    cursor = mydb.cursor();
    # --- 创建表
    # sql = """create table 
    # python(id int(3) zerofill auto_increment,
    # name varchar(15) not null,
    # age int,
    # constraint primary key(id))"""
    
    # --- 查看表
    # sql = """show tables"""
    # 为了防止sql注入攻击 我们可以将条件用占位符
    sql = """select * from python where age between %s and %s"""
    na = (15,25)
    # 
    # --- 插入数据
    # sql = """INSERT INTO python (name, age) VALUES (%s, %s)"""
    # val = ("知乎", 30)
    cursor.execute(sql,na)

    # 如果我们只想读取一条数据，可以使用 fetchone() 方法：
    # fetchall() 获取所有记录
    result = cursor.fetchall()
    for x in result:
        print(x)
    mydb.commit()    # 数据表内容有更新，必须使用到该语句

    # rowcount 获取改变条目数
    # print(cursor.rowcount, "记录插入成功。")
    
    #lastrowid 获取插入id
    print("1条插入成功,ID:",cursor.lastrowid)







