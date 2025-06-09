import psycopg2

db_name="employeedb"
db_user="postgres"
db_pass="Janhvi@123"
db_port="5432"

try:
    conn=psycopg2.connect(database=db_name,user=db_user,password=db_pass,port=db_port)
    print("Database connected successfully")

    try:
        cur=conn.cursor()
        cur.execute("""create table Employee(
        id Int NOT NULL PRIMARY KEY,
        name varchar(255),
        email varchar(255)
        )
        """)
        conn.commit()
        print("table create successfully")

    except:
        print("table already exists")

except:
    print("Database is not successfully")