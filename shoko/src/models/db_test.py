import psycopg2 as psy 

hostname= "35.229.79.41"
db_username = "postgres" 
db_password="i8KND8LOodrh2kbp"
dbname="postgres"

conn = psy.connect(dbname=dbname,user=db_username,host=hostname, password=db_password)

cur = conn.cursor()
cur.execute("INSERT INTO users VALUES ('TEST','TEST','TEST',0)")
