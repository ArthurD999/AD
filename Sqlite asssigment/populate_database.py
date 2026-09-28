import sqlite3

db_connection=sqlite3.connect("iris.db")
#cursor object
cursor = db_connection.cursor()

addData="""
insert into irisData (sepal_length,sepal_width,petal_length,petal_width,class) values (?,?,?,?,?)
"""
f=open("Iris - all-numbers.csv","r")
headerLine=f.readline()
for line in f:
    line=line.strip()#removes \m
    line=line.split(",")#creates a list-split on "comma"
    line = tuple(line)
    cursor.execute(addData,line)
    db_connection.commit()
#close the connection
cursor.close()

