# Employee_store
This project will take text file that contains inconsistant employee details as an input and store the cleaned information in mysql 

## Task details
Input file contains the data which is  ',' seprated.
First line in the file defines the column name of the DB table
1. Read the data from the file
2. Each row in the file has some inconsistant data. Like name with additional spaces, special char, etc
3. Cleanse the data by removing the special char and the spaces.
4. Create a table in DB with the name `emp_details`
5. Upload the data to the DB table.
6. If we re-run the program the contents should be over written.

## Stack details
```bash
Language : Python
Version : 3.7.3
```

## Installation
create virtual environment 
```bash
git clone https://github.com/goutham9032/Employee_store.git
cd Employee_store
```

```bash
pip3 install -r requirements.txt
```

## comand to run the script
```bash
Format : python3 task.py -u <username> -passwd <password -f <file path>
Eg: 
python3 task.py -u root -passwd mypassword -f sample_data.txt
```

## command help
```bash
python3 task.py -h
usage: task.py [-h] [-host HOST] [-p PORT] -u USER -passwd PASSWORD
               [-db DATABASE] [-t TABLE_NAME] -f FILE [-disp DISPLAY_RESULTS]

optional arguments:
  -h, --help            show this help message and exit
  -host HOST, --host HOST
                        host address where mysql is running
  -p PORT, --port PORT  port where mysql is running
  -u USER, --user USER  username for mysql
  -passwd PASSWORD, --password PASSWORD
                        password for mysql
  -db DATABASE, --database DATABASE
                        name of the database
  -t TABLE_NAME, --table_name TABLE_NAME
                        name of the table
  -f FILE, --file FILE  path of the file where employee details has stored
  -disp DISPLAY_RESULTS, --display_results DISPLAY_RESULTS
                        It will display all the emp details after storing in
                        db
```

## command expected output
```bash
('Id', 'First_name', 'Last_name', 'department', 'salary')
(1, 'Rohit', 'A', 'Tech', 20000)
(2, 'Vinay', 'Kumar', 'Tech', 30000)
(3, 'Manju', 'R', 'Tech', 60000)
(4, 'Nitin', 'SS', 'Support', 10000)
(5, '123 Satish', 'Y', 'Tech', 100500)
(6, 'Vinay', 'S', 'Support', 15000)
(7, 'Yatish', 'MN', 'Management', 160000)
(8, 'Sourabh', 'K', 'Tech', 6000)
(9, 'Vinay', 'Kumar', 'Support', 6000)
(10, 'Rohit', 'AA', 'Tech', 16000)
(13, 'Rahul', 'SS', 'Sales', 13100)
```
