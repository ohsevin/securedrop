import os
from base import BaseFlaskConfig

JOURNALIST_KEY='65A1B5FF195B56353CC63DFFCC40EF1228271441'#fingerprintofthepublickeyforencryptingsubmissions
SECUREDROP_ROOT=os.path.abspath('.securedrop')

class FlaskConfig(BaseFlaskConfig):
    DEBUG = True


### Database Configuration

# Default to using a sqlite database file for development
DATABASE_ENGINE = 'sqlite'
DATABASE_FILE=os.path.join(SECUREDROP_ROOT, 'db_development.sqlite')

# Uncomment to use mysql (or any other databaes backend supported by
# SQLAlchemy). Make sure you have the necessary dependencies installed, and run
# `python -c "import db; db.create_tables()"` to initialize the database

# DATABASE_ENGINE = 'mysql'
# DATABASE_HOST = 'localhost'
# DATABASE_NAME = 'securedrop'
# DATABASE_USERNAME = 'securedrop'
# DATABASE_PASSWORD = ''
