from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, User, Category, Item

engine = create_engine('sqlite:///catalog.db')
Session = sessionmaker(bind=engine)
session = Session()


# Categories
category1 = Category(name="Deciduous")
category2 = Category(name="Evergreen")
session.add(category1)
session.add(category2)
session.flush()

print("Category1 created on {}".format(category1.created_on))
print("Category2 created on {}".format(category2.created_on))

# Items
am_elm = Item(name="American Elm", photo_filename="american_elm.png",
    description="American Elm (Ulmus americana) can grow to 60 feet tall and 3 feet in diameter.  The wood is strong and difficult to split, which makes it idea for making saddle trees and for basket and crate veneer.", category_id=1, user_id=1)
bit_hick = Item(name="Bitternut Hickory", photo_filename="bitternut_hickory.png", description="Bitternut Hickory (Carya cordiformis) is a tall slender tree with a broad crown.  It can grow to 100 feet tall and 2-3 feet in diameter.  The wood is strong, heavy, and reddish brown in color.", category_id=1, user_id=1)

black_oak = Item(name="Black Oak", photo_filename="black_oak.png", description="Black Oak (Quercus velutina) can grow to 80 feet tall and 1-3 feet in diameter.  The wood is hard, stong, heavy, and checks easily", category_id=1, user_id=1)

black_hick = Item(name="Black Hickory", photo_filename="black_hickory.png", description="Black Hickory (Carya texana) grows on hillsides and sandy uplands.  This tree can grow to 75 feet tall and 2 feet in diameter.  The wood is hard, brittle, and makes good fuelwood.", category_id=1, user_id=1)

honey_locust = Item(name="Honeylocust", photo_filename="honeylocust.png", description="Honeylocust (Gleditsia triacanthos) can grow to 75 feet tall and 30 inches in diameter.  The wood is coarse-grained, strong, and moderately durable.", category_id=1, user_id=1)

loblolly = Item(name="Loblolly Pine", photo_filename="loblolly_pine.png", description="Loblolly Pine (Pinus taeda) is the most abundant commercial pine species in East Texas.  It can grow to 120 feet tall and 3-4 feet in diameter.  The wood is good for dimensional lumber, panels, and plywood veneer.", category_id=2, user_id=1)

session.bulk_save_objects([am_elm, bit_hick, black_oak, honey_locust, loblolly])
session.commit()

print("All items added")
