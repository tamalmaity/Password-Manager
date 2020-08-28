import mysql.connector
p = "mysql@123"
mydb = mysql.connector.connect(host='localhost', user='root',
                               password=p,
                               database='password_mg', autocommit = True)

mycursor = mydb.cursor()
first = 'gmail'
second = 'tamal@gmail.com'
third = '85^&'
sql = "UPDATE password_table SET Username = %s, Passwrd = %s WHERE Platform = %s"
adr = (second, third, first)

mycursor.execute(sql, adr)
