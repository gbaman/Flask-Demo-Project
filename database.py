from models import *



def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    Base.metadata.create_all(bind=engine)


def get_login_user_from_id(user_id):
    return db_session.query(LoginUser).filter(LoginUser.user_id == user_id).first()


def create_user(username, hash, salt):
    user = LoginUser(username=username, password_hash=hash, password_salt=salt)
    db_session.add(user)
    db_session.commit()