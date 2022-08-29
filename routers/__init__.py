from .supplier import *
from .catalog import *
from .product import *
from .category import *

from database import Base, engine

Base.metadata.create_all(bind=engine)