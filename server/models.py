from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Column, Integer, Float, String
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
class Earthquake(db.Model, SerializerMixin):
    '''Earthquake model in models.py'''

    __tablename__ = 'earthquakes'

    id = Column(Integer, primary_key=True)
    magnitude = Column(Float)
    location = Column(String)
    year = Column(Integer)

    def __init__(self, magnitude=None, location=None, year=None):
        self.magnitude = magnitude
        self.location = location
        self.year = year

    def to_dict(self):
        return {
            'id': self.id,
            'magnitude': self.magnitude,
            'location': self.location,
            'year': self.year
        }