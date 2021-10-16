import mysql.connector
import time,csv

connection=mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="open0813",
    database="youbike"
)

mycursor=connection.cursor()
sql = "INSERT INTO `bike_station` (`record_id`, `station_id`, `station_total_space`, `bike_left`, `free_space`) VALUES (%s, %s, %s, %s, %s)"
file=open("data_before_preprocessing/2021/10/1016/20211016_190025.csv","r",encoding="utf-8")
rows=csv.reader(file,delimiter=',')
next(rows)
for row in rows:
    total_space=int(row[5])
    left=int(row[6])
    free=int(row[10])
    mycursor.execute(sql,(row[0],row[4],total_space,left,free))
    connection.commit()
  
    
mycursor.close()
connection.close()