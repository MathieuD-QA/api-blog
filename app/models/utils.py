import databases
import sqlalchemy
DATABASE_URL=f"postgresql://postgres:postgrespw@localhost:55002/blog"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


