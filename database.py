# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Create an engine
engine = create_engine('sqlite:///database.db')

# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()


# Function to create a new user
def create_user(username, password):
    from models import User
    new_user = User(username=username, password=password)
    session.add(new_user)
    session.commit()
    print("User created successfully!")
#