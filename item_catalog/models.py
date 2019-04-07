from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from datetime import datetime

Base = declarative_base()


class User(Base):
    # represents the user database entity
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique=True, nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)


class Category(Base):
    # represents the category database entity
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)



class Item(Base):
    # represents the item database entity
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    photo_filename = Column(String(250))
    description = Column(String(180), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)

    category = relationship('Category', backref=backref('item', order_by=id))

    @property
    def serialize(self):
        """represents an object in JSON format for API enpoints"""
        return {
            'id':self.id,
            'name':self.name,
            'photo_filename':self.photo_filename,
            'description':self.description,
            'category_id':self.category_id
        }



engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)

