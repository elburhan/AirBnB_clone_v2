#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    # For DBStorage
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    # For FileStorage
    @property
    def cities(self):
        """Getter attribute that returns the list of City instances
        with state_id equals to the current State.id
        """
        from models import storage
        city_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
