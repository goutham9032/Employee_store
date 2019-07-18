# Python imports
import argparse
import re

# 3rd party imports
import mysql.connector

class LoadEmpDetails:
    '''
    This class will load employee details from text file to db
    '''
    def __init__(self, args):
        self.host = args.host
        self.port = args.port
        self.username = args.user
        self.password = args.password
        self.db = args.database
        self.table = args.table_name
        self.file_path = args.file
        self.disp = args.display_results

    def create_connection(self):
        self.conn = mysql.connector.connect(host=self.host,
                                       user=self.username,
                                       passwd=self.password,
                                       db=self.db,
                                       auth_plugin='mysql_native_password')
        self.cursor = self.conn.cursor()

    def execute_query(self, **query):
        self.create_connection()
        if 'values' in query:
            self.cursor.executemany(query['query'], query['values'])
            self.conn.commit()
        else:
            self.cursor.execute(query['query'])
        self.conn.close()

    def create_table(self):
        table_query = 'DROP TABLE IF EXISTS %s;\
                       CREATE TABLE %s ( \
                               Id int, \
                               First_name varchar(50), \
                               Last_name varchar(50),  \
                               department varchar(20), \
                               salary int)'%(self.table, self.table)
        self.execute_query(query=table_query)

    def get_cleaned_emp_details(self):
        emp_info = list()
        with open(self.file_path, 'r') as f:
             lines = f.readlines()[1:]
             for line in lines:
                 line = line.replace('\\n','').replace('\\r','')
                 cols = re.sub('[^a-zA-Z0-9, \\t\w\.]', '', line).split(',')
                 cleaned_cols = [i.strip() for i in cols]
                 try:
                    _id, f_name, l_name, dept, sal = cleaned_cols
                 except Exception as e:
                    continue
                 emp_info.append(tuple(cleaned_cols))
        return emp_info

    def upload_emp_details_to_db(self):
        insert_query = "INSERT INTO EMP_DETAILS (id, first_name, last_name, department, salary) \
                                              VALUES (%s, %s, %s, %s, %s)"
        cleaned_emp_details = self.get_cleaned_emp_details()
        self.execute_query(query=insert_query, values=cleaned_emp_details)

    def display_uploaded_results(self):
        self.create_connection()
        self.cursor.execute('select * from %s'%(self.table))
        print(self.cursor.column_names)
        for i in self.cursor.fetchall():
            print(i)

    def run(self):
        self.create_table()
        self.upload_emp_details_to_db()
        if self.disp:
           # If display results is true it will display all results stored from the table
           self.display_uploaded_results()

def define_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-host", "--host", type=str, default="localhost",
                        help="host address where mysql is running")
    parser.add_argument("-p", "--port", type=int, default=3306,
                        help="port where mysql is running")
    parser.add_argument("-u", "--user", type=str, required=True,
                        help="username for mysql")
    parser.add_argument("-passwd", "--password", required=True,
                        help="password for mysql")
    parser.add_argument("-db", "--database", default="EMP",
                        help="name of the database")
    parser.add_argument("-t", "--table_name", default="EMP_DETAILS",
                        help="name of the table")
    parser.add_argument("-f", "--file", required=True,
                        help="path of the file where employee details has stored")
    parser.add_argument("-disp", "--display_results", default=True, type=bool,
                        help="It will display all the emp details after storing in db")

    args = parser.parse_args()
    return args

if __name__=="__main__":
   args = define_args()
   emp = LoadEmpDetails(args=args)
   emp.run()
