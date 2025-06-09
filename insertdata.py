import psycopg2

db_name="employeedb"
db_user="postgres"
db_pass="Janhvi@123"
db_port="5432"

try:
    conn=psycopg2.connect(database=db_name,user=db_user,password=db_pass,port=db_port)
    print("Database connected successfully")

    cur=conn.cursor()
    cur.execute("""
    insert into employee (id,name,email)values
    (1,'janhvi kudke','janhvi@gmail.com'),
    (2,'varsha more','varsha@gmail.com'),
    (3,'yogita ghule','yogita@gmail.com')
    """)
    conn.commit()
    conn.close()

except:
    print("Database is not successfully")