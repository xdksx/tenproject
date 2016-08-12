#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

db = MySQLdb.connect("localhost","root","123456","stream" )

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS stream_manage3")


sql = """CREATE TABLE stream_manage3(
         streamkey  VARCHAR(20) NOT NULL primary key,
         timestamp varchar(20),
         country varchar(20),
         province varchar(20), 
         carrier varchar(20),
         platform varchar(20),
         stream_type int,
         numofstream int
)"""

cursor.execute(sql)

# 
db.close()
