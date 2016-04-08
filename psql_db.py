import pandas as pd
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
import datetime

class db():
	def __init__(self, host, username, password, dbname):
		'''
		establishes connection with database; creates sqlalchemy engine; 
		prepares sqlalchemy metadata.
		'''
		self.host=host
		self.username=username
		self.password=password
		self.dbname=dbname

		#make engine & create metadata object
		self.engine=sqlalchemy.create_engine('postgresql://' + 
			username + ':' + password +'@' + host + '/' + dbname)
		self.Base=declarative_base()
		self.connection=self.engine.connect()
		self.Base.metadata.bind=self.engine

	def show_tables(self):
		'''
		show all the tables in the database
		'''
		m=self.Base.metadata
		m.reflect(bind=self.engine)
		df=pd.DataFrame({'Table':[table for table in m.sorted_tables]})
		return df

	def describe_table(self, table_name):
		'''
		lists the columns of the table
		'''
	 	temptbl = sqlalchemy.schema.Table(table_name, self.Base.metadata, autoload=True, autoload_with=self.engine)
	 	df=pd.DataFrame({'Columns': [names for names in temptbl.columns]})
	 	return df


	def get_trmi(self, table_name, asset=None , start_date='2005-01-01', end_date=datetime.datetime.today()):
	    '''returns a pandas Dataframe of the table specified. 
	        uses "Date" as index, if present'''
	    date_range='WHERE "Date">= \'' + start_date + '\' and "Date"<= \'' + str(end_date) + '\''
	    try: 
	        ass_='and "Asset"=\'' + asset + '\''
	    except:
	        ass_=''
	    tbl=pd.read_sql('SELECT * FROM %s %s %s' %(table_name, date_range, ass_), self.engine )
	    try:
	    	tbl.index=tbl.windowTimestamp
	    except: 
	    	pass
	    return tbl

	def get_table(self, table_name):
		'''
		returns a pandas dataframe of the table inquired
		'''
		 tbl=pd.read_sql('SELECT * FROM %s' %table_name, self.engine)
		 return tbl



	#This would ideally create objects for all tables in the database, but 
	#I couldn't get it to work. 
	#Possibly because the tables don't have a primary key(?)
	#Automap with database
	# def automapbase():
	# 	engine=sqlalchemy.create_engine('postgresql://' + 
	# 		username + ':' + password +'@' + host + '/' + dbname)
	# 	Base=automap_base()
	# 	Base.prepare(engine, reflect=True)
	# 	return Base