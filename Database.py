import mysql.connector
from datetime import datetime 
global mydb,cursor;

mydb= mysql.connector.connect(host="localhost",user="root")


def connection():
	
	if mydb.is_connected():
		print("Connection Established");
	else:
		print("Not Conected, check ..")

def create_database():
	if mydb.is_connected():
		cursor=mydb.cursor();
		cursor.execute("CREATE DATABASE TEST_181040012")
		print("Database created");

	#mydb.close()
	
def create_table():
	mydb= mysql.connector.connect(host="localhost",user="root",database="TEST_181040012")

	if mydb.is_connected():
		cursor = mydb.cursor();
		cursor.execute("CREATE TABLE register_181040012(id INT(20) PRIMARY KEY,fname VARCHAR(50), lname VARCHAR(50),dob DATE)")
		print("Table created successfully")

def insertvalue(id,fname,lname,dob):
	mydb= mysql.connector.connect(host="localhost",user="root",database="TEST_181040012")

	if mydb.is_connected():
		query = "INSERT INTO register_181040012(id,fname,lname,dob) VALUES(%s,%s,%s,%s)"
		details= (id,fname,lname,dob);
		print(details)
		cursor = mydb.cursor();	
		cursor.execute(query,details);
		mydb.commit();
		print("Inserted successfully")

def retreiveall():
	mydb= mysql.connector.connect(host="localhost",user="root",database="TEST_181040012")

	query = "SELECT * FROM register_181040012";
	cursor =  mydb.cursor();
	cursor.execute(query)
	rows = cursor.fetchall();
	for row in rows:
		print(row);
def truncate_table():
	mydb= mysql.connector.connect(host="localhost",user="root",database="TEST_181040012")

	query="DROP TABLE register_181040012"
	cursor=mydb.cursor();
	cursor.execute(query)
	print("Table Dropped")
def main():
	connection();
	
	while True:
		print("\nEnter your choice:");
		print("createdatabase-->1:")
		print("create table-->2:")
		print("insertion-->3:")
		print("retrieve details-->4")
		print("truncatetable-->5")
		print("Quit-->q")
		choice = input("Enter the option:")
		if choice == '1':
			create_database()
		if choice == '2':
			create_table()
		if choice == '3':
			id=input("Enter id:");
			fname=input("enter first name:");
			lname=input("enter last name:");
			dob=input("enter Date of birth in (YYYY-MM-DD)format:");
			insertvalue(id,fname,lname,dob)
		if choice=='4':
			retreiveall()
		if choice=='5':
		 	truncate_table()
		if choice == 'q':
			sys.exit()
		



if __name__ == "__main__":
	main();
	


