from sqlalchemy.ext.declarative import declarative_base 

DATABASE_URL = f'postgresql://manager:manager1@postgres-db:5432/taskmanagerdatabase'
Base = declarative_base()


