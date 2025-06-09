import psycopg2

db_name="employeedb"
db_user="postgres"
db_pass="Janhvi@123"
db_port="5432"

try:
    conn=psycopg2.connect(database=db_name,user=db_user,password=db_pass,port=db_port)
    print("Database connected successfully")
    cur=conn.cursor()
    cur.execute("update employee set email='janhvi11@gmail.com' where id =1")
    conn.commit()
    print("data updated successfully")
    print("total row affected "+str(cur.rowcount))
    conn.close()
except:
    print("Database is not successfully")