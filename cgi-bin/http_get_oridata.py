#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cgi, os
import cgitb; cgitb.enable()
import MySQLdb
import types

db=MySQLdb.connect("localhost","root","123456","stream")

form = cgi.FieldStorage()

# get filename
fileitem = form['filename']

# file upload?
if fileitem.filename:
   # set file path 
   fn = os.path.basename(fileitem.filename)
   open('/tmp/' + fn, 'wb').write(fileitem.file.read())

   message = '文件 "' + fn + '" 上传成功'
   
   
   revfile=open('/tmp/'+fileitem.filename,'r')
   line=revfile.readline()
   pa=line.split(' ')
   cursor=db.cursor()
   type1=int(pa[6])
   num=int(pa[7])
   #sql="""INSERT INTO stream_manage3 (streamkey,timestamp,country,\
    #    province,carrier,platform,stream_type,numofstream) \
     #   VALUES('%s','%s','%s','%s','%s,'%s','%d','%d')"""%\
      #  (pa[0],pa[2],pa[3],pa[4],pa[5],pa[6],7,8)
   try:
       cursor.execute('INSERT INTO stream_manage3 \
       VALUES("%s","%s","%s","%s","%s","%s","%d","%d")'%\
       (pa[0],pa[1],pa[2],pa[3],pa[4],pa[5],type1,num))
       db.commit()
   except:
       db.rollback()   
   revfile.close()
   db.close()
   
else:
   message = '文件没有上传'
   
print """\
Content-Type: text/html\n
<html>
<head>
<meta charset="utf-8">
<title>dataupload_ex</title>
</head>
<body>
   <p>%s</p>
   <p>%s</p>
   <p>%s</p>
   <p>%s</p>
   <p>%s</p>
   <p>%s</p>
   <p>%s</p>
   <p>%s</p>
</body>
</html>

""" % (message,pa[0],pa[2],pa[3],pa[4],pa[5],pa[6],pa[7])
