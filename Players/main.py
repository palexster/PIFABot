from sqlalchemy import String,true
from flask import Flask
from sqlalchemy import Column, Date, DateTime, Float, Integer, Unicode
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship
from sqlalchemy.orm import scoped_session, sessionmaker
import flask_restless
import flask

app = flask.Flask(__name__)
engine = create_engine('sqlite:////tmp/testdb.sqlite', convert_unicode=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
mysession = scoped_session(Session)

Base = declarative_base()
Base.metadata.bind = engine

class Players(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    position = Column(Integer)
    club = Column(String(3))
    fantaMedia =  Column(Float)
    gol = Column(Integer)
    ammonizioni = Column(Integer)
    espulsioni = Column(Integer)
    assists = Column(Integer)
    mediaVoto = Column(Float)
    presenze = Column(Integer)
    golSubiti = Column(Integer, nullable=true)
    PortiereImbattuto = Column(Integer, nullable=true)
    rigoriSegnati = Column(Integer, nullable=true)
    rigoriParati = Column(Integer, nullable=true)
    rigoriSbagliati = Column(Integer, nullable=true)

    # jerseyNumber = Column(String(100))
    # dateOfBirth = Column(String(100))
    # nationality = Column(String(100))
    # contractUntil = Column(String(100))
    # surname = Column(String(100))
#    credits = Column(String(100))

    def __init__(self, name, position, club, FantaMedia, Gol, MediaVoto,
                 Presenze, golSu, pi, rigFa, rigPa, Amm, Esp, Ass, rigSb):
        self.name = name
        self.position = position
        self.club = club
        self.fantaMedia = FantaMedia
        self.gol = Gol
        self.ammonizioni = Amm
        self.espulsioni = Esp
        self.assists = Ass
        self.mediaVoto = MediaVoto
        self.presenze = Presenze
        self.golSubiti = golSu
        self.PortiereImbattuto = pi
        self.rigoriSegnati = rigFa
        self.rigoriParati = rigPa
        self.rigoriSbagliati = rigSb

# Create the database tables.
Base.metadata.create_all()

# Create the Flask-Restless API manager.
manager = flask_restless.APIManager(app, session=mysession)


# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
blueprint = manager.create_api(Players, methods=['GET', 'POST', 'DELETE','PUT'])
print(blueprint)

# start the flask loop
#app.run(host='0.0.0.0',port=5500)