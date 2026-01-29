import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///02_SQLite/movies.db', echo=True)

metadata = sqlalchemy.MetaData()

movies_table = sqlalchemy.Table(
    "Movies",
    metadata,
    sqlalchemy.Column("title", sqlalchemy.Text),
    sqlalchemy.Column("director", sqlalchemy.Text),
    sqlalchemy.Column("year", sqlalchemy.Integer)
)

metadata.create_all(engine)

with engine.connect() as conn:
    result = conn.execute(sqlalchemy.select(movies_table))
    for row in result:
        print(row)