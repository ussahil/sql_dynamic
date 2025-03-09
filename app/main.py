import psycopg2
from psycopg2 import sql

def create_client_db_and_table(client_name):
  # Format database to avoid special chars
  db_name = f"db_{client_name.lower().replace(' ','_')}"
  
  # Connect to default postgres database
  conn = psycopg2.connect(dbname='postgres',user='postgres',password='123',host='localhost')
  conn.autocommit = True
  cur = conn.cursor()
  
  # Create a new Database for the client
  try:
    cur.execute(sql.SQL("Create Database {}").format(sql.Identifier(db_name)))
    print(f"Database {db_name} created successfully")
  except pycopg2.errors.DuplicateDatabase:
    print(f"Database {db_name} exists change client's name")
    
  cur.close()
  conn.close()
  
  # Connect to newly created db to create table
  conn = psycopg2.connect(dbname=db_name,user="postgres",password="123",host='localhost')
  cur = conn.cursor()
  
  # Creating the reviews table
  cur.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
      s_no SERIAL PRIMARY KEY,
      review TEXT NOT NULL
    );
    """)
  conn.commit()
  print(f"Table 'reviews' has been created in database {db_name}")
    
  cur.close()
  conn.close()
  
  
if __name__ == '__main__':
  client_name = input("Enter client's name:")
  create_client_db_and_table(client_name)