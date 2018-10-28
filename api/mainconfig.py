import json
import uuid
from flask import render_template_string, render_template
from .ini_api import IAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api import dbclasses as DB


class MainConfig(object):

    def getDBSess(self):
        engine = create_engine(IAPI.getDBLink(), convert_unicode = True)
        Session = sessionmaker(engine)
        sess = Session()
        return sess

    def logoutDeleteUserInfo(self, in_sess_id):
        sess = self.getDBSess()
        x = sess.query(DB.RSession).filter(DB.RSession.sess_id == str(in_sess_id)).first()
        uid = x.user_id
        #RAPI.deleteKey(sess_id)
        #ME.userName = ''
        return True

    def checkSessionID(self, in_sess_id):

        sess = self.getDBSess()
        x = sess.query(DB.RSession).filter(DB.RSession.sess_id == str(in_sess_id)).first()
        if x is None:
            return False
        return True

    def startSession(self, login, password):
        if login == '' or password == '': return None
        sess = self.getDBSess()

        x = sess.query(DB.RUser).filter(DB.RUser.username == login).filter(DB.RUser.userpass == password).first()
        if x is None:
            return None

        SessID = uuid.uuid4()
        sess.add(DB.RSession(user_id = x.id, sess_id = str(SessID)))
        sess.commit()
        return SessID

    ################################################

MCFG = MainConfig()
