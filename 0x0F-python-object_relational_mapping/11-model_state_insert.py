#!/usr/bin/python3
"""a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa"""

"""11-model_state_insert.py"""

if __name__ == '__main__':

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.schema import Table
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    new = State(name='Louisiana')
    session.add(new)
    session.commit()
    print(new.id)
    session.close()
