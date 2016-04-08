# psql_db
If you don't want to deal with accessing the database/querying and would rather just download the whole table and work locally, this module is for you!

The psql_db module contains the following objects:

The class db(host, username, password, dbname):
  Initialization of a db object connects you to the database using sqlalchemy. 
  It also establishes a sqlalchemy.engine object, as well as prepares a sqlalchemy 
  metadata object. 

The show_tables() method: 
  Shows all the tables in the database.

The describe_table(table_name) method:
  Takes in table_name (string) and 
  returns a pandas dataframe that contains all the columns of the table inquired about.

The get_trmi(table_name, asset=None, start_date='2005-01-01', end_date=datetime.datetime.today()) method:
  Takes table_name (string), asset (string), start_date (string), end_date string) and 
  returns a pandas dataframe of the table. 
  Only applicable to trmi tables (or tables with an "Asset" and "date" column).

The get_table(table_name) method:
  Takes table_name (string) and returns pandas dataframe of the table desired.
  A more general version of get_trmi. Applicable to any table.
  Note that entire table will be selected. 
  
