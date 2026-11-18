# db_util.py
"""
智能体豆包生成的数据库工具类
"""
import pymysql
from pymysql.err import OperationalError, ProgrammingError
from typing import Optional, List, Dict, Tuple


class DBUtil:
    _instance = None
    _conn = None

    def __new__(cls, *args, **kwargs):
        """单例模式，全局共用一个数据库连接对象"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, host: str, port: int, user: str, password: str, database: str, charset: str = "utf8mb4"):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset

    def connect(self):
        """建立数据库连接"""
        if self._conn is None or self._conn.open is False:
            try:
                self._conn = pymysql.connect(
                    host=self.host,
                    port=self.port,
                    user=self.user,
                    password=self.password,
                    database=self.database,
                    charset=self.charset,
                    autocommit=False  # 关闭自动提交，事务可控
                )
            except OperationalError as e:
                raise ConnectionError(f"数据库连接失败：{e}")
        return self._conn

    def close(self):
        """关闭连接"""
        if self._conn and self._conn.open:
            self._conn.close()
            self._conn = None

    def select_one(self, sql: str, params: Tuple = ()) -> Optional[Dict]:
        """
        查询单条数据，返回字典格式
        :param sql: select sql语句
        :param params: 参数元组
        :return: 单行字典 / None
        """
        conn = self.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql, params)
            return cursor.fetchone()
        except Exception as e:
            raise ProgrammingError(f"查询单条失败：{e}")
        finally:
            cursor.close()

    def select_all(self, sql: str, params: Tuple = ()) -> List[Dict]:
        """
        查询多条数据，返回字典列表
        """
        conn = self.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql, params)
            return cursor.fetchall()
        except Exception as e:
            raise ProgrammingError(f"查询多条失败：{e}")
        finally:
            cursor.close()

    def execute(self, sql: str, params: Tuple = ()) -> int:
        """
        执行 insert / update / delete
        :return: 影响行数
        """
        conn = self.connect()
        cursor = conn.cursor()
        try:
            row = cursor.execute(sql, params)
            conn.commit()
            return row
        except Exception as e:
            conn.rollback()
            raise ProgrammingError(f"执行SQL失败，已回滚：{e}")
        finally:
            cursor.close()

    def insert_return_id(self, sql: str, params: Tuple = ()) -> int:
        """插入数据，返回自增主键id"""
        conn = self.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, params)
            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            conn.rollback()
            raise ProgrammingError(f"插入失败，已回滚：{e}")
        finally:
            cursor.close()

    def __enter__(self):
        """上下文管理器，with语法支持"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# ========== 示例配置与调用demo ==========
if __name__ == '__main__':
    # 初始化数据库对象，正式项目建议抽离配置文件 config.yaml
    db = DBUtil(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="123456",
        database="test_db"
    )

    # 1. 查询单条
    res1 = db.select_one("select * from user where id = %s", (1,))
    print("单条查询：", res1)

    # 2. 查询多条
    res2 = db.select_all("select * from user limit %s", (5,))
    print("多条查询：", res2)

    # 3. 新增
    new_id = db.insert_return_id("insert into user(name,age) values (%s,%s)", ("张三", 22))
    print("新增主键id：", new_id)

    # 4. 修改
    update_rows = db.execute("update user set age=%s where id=%s", (23, new_id))
    print("更新行数：", update_rows)

    # 5. 删除
    del_rows = db.execute("delete from user where id=%s", (new_id,))
    print("删除行数：", del_rows)

    db.close()
