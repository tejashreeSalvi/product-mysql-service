import json
import mysql.connector

# Connect to the MySQL database
cnx = mysql.connector.connect(
    user='root',
    password='Mysql@123',
    database='teju1'
)

print("Connection:", cnx)

# Load the csvjson.json file into a Python dictionary
with open('csvjson.json') as f:
    data = json.load(f)

print('data:', data, len(data))

# Create the MySQL table if it does not already exist
table_name = 'productList'
cursor = cnx.cursor()


columns = ', '.join([col.replace(' ', '_') for col in data[0].keys()])
values = ', '.join(['%s'] * len(data[0]))
print("colums:", columns)
print("values:", values)

# create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
# cursor.execute(create_table_sql)
print("Cursor:", cursor)

# Insert the data into the MySQL table
insert_data_sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
print(data)

for i, record in enumerate(data):
    try:
        print("Index:", i)
        cursor.execute(insert_data_sql, list(record.values()))
    except Exception as ex:
        print("Exception occurred:", ex)

# Commit the changes and close the cursor
cnx.commit()
cursor.close()

# Close the connection to the MySQL database
cnx.close()
print("Connection closed!!")
