from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, relationship

engine = create_engine('sqlite:///demo.db?check_same_thread=False')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
metadata = Base.metadata


class LoginUser(Base):

    __tablename__= "login_users"
    user_id = Column(Integer, autoincrement=True, primary_key=True, unique=True, nullable=False)
    username = Column(String(30), nullable=False, unique=True)
    password_hash = Column(String(100), nullable=False)
    password_salt = Column(String(100), nullable=False)


Base.metadata.create_all(engine)