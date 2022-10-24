

# Python 3.9.7
#
# Author: Spencer Davis\
#
# Purpose: Database Submission Assigment in the Tech Academy's Python Course.
#

import sqlite3 

conn = sqlite3.connect('test1.db') #Connect to sqllite3, create database

with  conn:
    cur = conn.cursor()
    #Create primary integer field and a field with the data type string
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file STRING)")
    conn.commit()
conn.close()

conn = sqlite3.connect('test1.db')

fileList = ('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
# Add files from the list
# which end with a .txt file
with  conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_files(col_file)VALUES (?)", \
                ('Hello.txt'))
    cur.execute("INSERT INTO tbl_files(col_file)VALUES (?)", \
                ('World.txt'))
    conn.commit()
conn.close()


conn = sqlite3.connect('test1.db')

with  conn:
    cur = conn.cursor()
    cur.execute("SELECT col_file FROM tbl_files WHERE col_files = ' 'Hello.txt','World.txt''") 
    varFile = cur.fetchall()
    for item in varFile:
        msg = "Qualifying Documents: {} \nLast Name: {} \nEmail: {}".format(item[0],item[1])
    print(msg)

    
