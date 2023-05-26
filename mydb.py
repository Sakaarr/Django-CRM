import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'EDSPerfect#5678',

)
#prepare a cursoor object
cursorObject = dataBase.cursor()

#create a database

cursorObject.execute("CREATE DATABASE sakardbms")

print("All Done")