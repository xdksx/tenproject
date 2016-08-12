#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb,cgi,cgitb


db = MySQLdb.connect("localhost","root","123456","stream" )

cursor = db.cursor()

sql = """INSERT INTO stream_manage3(streamkey,timestamp,
         country,province,carrier,platform,stream_type,numofstream)
         VALUES ('000000001','4511','china','guangdong','chinamobile','douyu',1,12)"""
try:
   cursor.execute(sql)
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()


db.close()
