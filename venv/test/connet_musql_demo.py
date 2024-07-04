# -*- coding: utf-8 -*-
"""
-
Author:
Date:
"""

import mysql.connector


def fetch_all_data_as_dict(database, table, username, password, host='localhost'):
    # 连接到数据库
    cnx = mysql.connector.connect(user=username, password=password,
                                  host=host,
                                  database=database)
    if cnx.is_connected():
        print("数据库连接成功")

    try:
        # 创建一个字典类型的游标
        cursor = cnx.cursor(dictionary=True)

        # 编写SQL查询语句
        # query = f"SELECT * FROM {table}"

        # 编写SQL查询语句，使用LIMIT 10来获取前10条记录
        query = f"SELECT * FROM {table} LIMIT 10"

        # 执行SQL查询
        cursor.execute(query)



        # 获取所有行并将结果存储在一个列表中，列表中的每个元素都是一个字典
        rows = cursor.fetchall()

        return rows

    finally:
        # 不论是否发生异常，都要确保关闭游标和连接
        cursor.close()
        cnx.close()


# 使用函数获取数据
host = '139.9.220.172'  # 数据库主机地址
database_name = 'dvt-server-db'  # 数据库名称
table_name = 't_xrui_dvt_online'  # 数据表名称
username = 'root'  # 数据库用户名
password = 'P6ss123456'  # 数据库密码

data = fetch_all_data_as_dict(database_name, table_name, username, password, host=host)

print(data)
# # 打印获取到的数据
# for row in data:
#     print(row)
