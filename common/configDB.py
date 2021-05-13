import pymysql
import readConfig

class DBsql():
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def ConnectDB(self):
        global conn
        try:
            conn = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except:
            print('数据库连接失败')
        return conn

    def SelectDB(self,query):
        conn = self.ConnectDB()
        #获取游标
        cur = conn.cursor()
        cur.execute(query)
        while 1:
            res=cur.fetchone()
            if res is None:
                #表示已经取完结果集
                break
            print (res)
        conn.commit()
        conn.close()
        print('sql执行成功')

     #单条数据查询方法
    def Select(self,key,table,conditions,value):
        sql = 'select  %s ' % key
        sql += ' from %s ' % table
        sql += " where %s = '%s'" % (conditions,value)
        # query = "SELECT car_model FROM vehicle_license_apply_info WHERE id ='02f566b502c00000';"
        conn = self.ConnectDB()
        # 获取游标
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()
        print('sql执行成功')
        return cur.fetchall()

    #删除数据库数据，清理测试脏数据
    def Delete(self,table,conditions,value):
        sql = 'delete '
        sql += ' from %s ' % table
        sql += " where %s = '%s';" % (conditions, value)
        print(sql)
        conn = self.ConnectDB()
        # 获取游标
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()
        print('sql执行成功')
        return cur.fetchall()

if __name__ == '__main__':
    a = "SELECT car_model FROM vehicle_license_apply_info WHERE id ='02f566b502c00000';"
    print(a)
    a = DBsql(readConfig.ReadConfig().get_content('DATABASE','host'),
            readConfig.ReadConfig().get_content('DATABASE','user'),
            readConfig.ReadConfig().get_content('DATABASE','password'),
            readConfig.ReadConfig().get_content('DATABASE','databaseCar')).\
        Delete('vehicle_license_apply_info','id','02b64d4facc00000')
    print(a)

#delete from `vehicle-license`.vehicle_license_apply_info
#WHERE id = '02f7947bec800000'