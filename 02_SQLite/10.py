from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Text, insert, select

engine = create_engine('sqlite:///02_SQLite/users.db', echo=True)
metadata = MetaData()
users_table = Table(
    "Users",
    metadata,
    Column("User_Id", Integer, primary_key=True),
    Column('First_Name', Text),
    Column('Last_Name', Text),
    Column('Email_Address', Text)
)

metadata.create_all(engine)

new_records = [
    {"First_Name": "Gustavo", "Last_Name": "Carvalho", "Email_Address": "gc@gmail.com"},
    {"First_Name": "Laercio", "Last_Name": "Dias", "Email_Address": "ld@hotmail.com"},
    {"First_Name": "Isabele", "Last_Name": "Veiga", "Email_Address": "iv30@gmail.com"},
    {"First_Name": "Monica", "Last_Name": "Campos", "Email_Address": "mcampos@live.com"},
    {"First_Name": "Paulo", "Last_Name": "Carvalho", "Email_Address": "carvalhopaulo@gmail.com"},
]

with engine.connect() as conn:
    stmt = insert(users_table).values(new_records)
    conn.execute(stmt)

    conn.commit()

    result = conn.execute(select(users_table.c.Email_Address))
    for row in result:
        print(row)
