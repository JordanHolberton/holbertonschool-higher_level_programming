#!/usr/bin/python3

"""write a script 14-model_city_fetch_by_state.py that prints all
City objects from the database hbtn_0e_14_usa:"""

import sys
from model_state import State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id).all()
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
