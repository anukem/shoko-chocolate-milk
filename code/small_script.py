import psycopg2 as psy 

# set all vars for connection
hostname = "35.229.79.41"
username = "postgres"
password = "i8KND8LOodrh2kbp"
db_name = "postgres"

conn = psy.connect(host=hostname, user=username, password=password, dbname=db_name)

conn.close()
