# Load CSV data into MySQL in Python
```python
import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='mydb')
cursor = mydb.cursor()

csv_data = csv.reader(file('students.csv'))
for row in csv_data:

    cursor.execute('INSERT INTO testcsv(names, \
          classes, mark )' \
          'VALUES("%s", "%s", "%s")', 
          row)
#close the connection to the database.
mydb.commit()
cursor.close()
print "Done"

```


```
pip install pymysql

```

```python
import pymysql
import sys

def csv_to_mysql(load_query, host, user, password):

    try:
        con = pymysql.connect(host=host,
                                user=user,
                                password=password,
                                autocommit=True,
                                local_infile=1)
        print('Connected to DB: {}'.format(host))
        # Create cursor and execute Load SQL
        cursor = con.cursor()
        cursor.execute(load_query)
        print('Succuessfully loaded the table from csv.')
        con.close()
        
    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)


load_query = """LOAD DATA LOCAL INFILE 'employee.csv' INTO TABLE company.employee\
 FIELDS TERMINATED BY ',' ENCLOSED BY  '"' IGNORE 1 ROWS;"""
host = 'localhost'
user = 'root'
password = ''
csv_to_mysql(load_query, host, user, password)

```

