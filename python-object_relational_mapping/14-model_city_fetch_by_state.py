#!/usr/bin/python3
"""Fetches all City objects from the database hbtn_0e_14_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Create an engine that connects to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a Session
    session = Session()
    
    # Query all City objects and join with State to get the state name
    results = session.query(City, State).join(State).order_by(City.id).all()
    
    # Print the results
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")
    
    # Close the session
    session.close()
