from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


# створення двигуна
# engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('sqlite:///C:/Users/kid/PycharmProjects/my_first_repo/data.db', echo=True)

# Створення базового класу для відображення вмісту таблиці БД
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name='{self.name}', age='{self.age}')>"


Base.metadata.create_all(bind=engine)

# Створення классу сесії
Session = sessionmaker(bind=engine)
# Створення екзимпляру класу Session
session = Session()

user1 = User(name="John Cena", age=51)

user2 = User(name="Margareth Johnson", age=43)

session.add(user1)
session.add(user2)

session.commit()

users = session.query(User).all()
for user in users:
    print(user)
