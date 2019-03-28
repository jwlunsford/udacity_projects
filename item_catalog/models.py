from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import realtionship, backref
from sqlalchemy import create_engine

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

    def __repr__(self):
        # used to represent the User in printed output, primarily for
        # debugging
        return "User(username={self.username}, " \
                    "email={self.email})".format(self=self)


class Category(Base):
    # represents the category database entity
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)

    def __repr__(self):
        # used to represent the Category in printed output, primarily for
        # debugging
        return "Category(name={self.name})".format(self=self)


class Item(Base):
    # represents the item database entity
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    photo = Column(String(250))
    description = Column(String(250), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)

    category = relationship('Category', backref=backref('items', order_by=id))

    def __repr__(self):
        # used to represent the Item in printed output, primarily for
        # debugging
        return "Item(name={self.name}, photo={self.photo}, " \
                    "description={self.description}, " \
                    "category_id={self.category_id})".format(self=self)



engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)

