import psycopg2

db_name="employeedb"
db_user="postgres"
db_pass="Janhvi@123"
db_port="5432"

try:
    conn=psycopg2.connect(database=db_name,user=db_user,password=db_pass,port=db_port)
    print("Database connected successfully")
    cur=conn.cursor()
    cur.execute("select * from employee")
    rows=cur.fetchall()
    for data in rows:
        print("Id:"+ str(data[0]))
        print("Name:"+ data[1])
        print("Email:"+ data[2])
    print("data fetched successfully")
    conn.close()

except:
    print("Error")
