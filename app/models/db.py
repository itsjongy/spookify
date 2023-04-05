from flask_sqlalchemy import SQLAlchemy
import os
from enum import Enum

class Environment(Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"

environment = os.environ.get("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

db = SQLAlchemy()

def add_prefix_for_prod(attr):
    """
    Adds schema prefix to the attribute name in production environment.
    """
    return f"{SCHEMA}.{attr}" if environment == Environment.PRODUCTION.value else attr
