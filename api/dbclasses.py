from sqlalchemy import Column, Integer, String, ForeignKey, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()
####################################### Class declarations


class RSession(Base):
    __tablename__ = 'rsession'
    id = Column(Integer, primary_key=True)
    sess_id = Column(String(50))
    user_id = Column(Integer, ForeignKey('ruser.id'))

    def __repr__(self):
        return self.sess_id


class RUser(Base):
    __tablename__ = 'ruser'
    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    userpass = Column(String(100))
    userinfo = Column(String(200))
    isadmin = Column(Integer, default=0)

    def __repr__(self):
        return self.username + '(' + self.userinfo + ')'

class RFiles(Base):
    __tablename__ = 'rfiles'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    user_id = Column(Integer, ForeignKey('ruser.id'))
    params = Column(String(100))
    image = Column(BLOB)



def engine():
    return create_engine('sqlite:///database.db', convert_unicode=True)

##############################
#engine = create_engine('sqlite:///database.db', convert_unicode=True)
#Base.metadata.create_all(bind=engine)
#engine.dispose()
