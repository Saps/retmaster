from flask import render_template, render_template_string
from flask import request, session, redirect, url_for, json

from api import ini_api as inapi
from api import MCFG
import json

class MainResource():

    def defaultPage(self):
        return redirect(url_for('resrc.loginWindow'))

    def loginWindow(self):

        #return render_template('lk_login.html')

        lg = None
        if inapi.IAPI.config.has_option('OTHERS', 'deflogin'):
            lg = inapi.IAPI.config.get('OTHERS', 'deflogin')
        lp = None
        if inapi.IAPI.config.has_option('OTHERS', 'defpassw'):
            lp = inapi.IAPI.config.get('OTHERS', 'defpassw')

        if 'sess_id' in session:
            ivi = "../" + inapi.IAPI.config.get('OTHERS', 'mainroute')
            return redirect(ivi)

        if request.method != 'POST':
            if not (lg and lp):
                plogin = render_template('lk_login.html')
                return plogin
        else :
            lg = request.form['lk_username']
            lp = request.form['lk_password']

        x = MCFG.startSession(lg, lp)
        if x is not None:
            session['sess_id'] = x
            MCFG.userName = lg
        else:
            session.pop('sess_id', None)
            plogin = render_template('lk_login.html')
            return plogin
        ivi = "../" + inapi.IAPI.config.get('OTHERS', 'mainroute')
        return redirect(ivi)


    def logoutWindow(self):
        if 'sess_id' in session:
            MCFG.logoutDeleteUserInfo(session['sess_id'])
            session.pop('sess_id', None)
        return redirect(url_for('resrc.defaultPage'))

    def mainPage(self):
        if 'sess_id' not in session:
            return redirect(url_for('resrc.loginWindow')) #, next=request.url))
        if not MCFG.checkSessionID(session['sess_id']):
            return redirect(url_for('resrc.loginWindow'))  # , next=request.url))
        return render_template('main.html',)

        #return "<H1>IN MAIN</H1>"


    def checkImage(self):
        ar = {}
        ar['cid'] = "0000"
        ar['tid'] = "0102"
        return json.dumps(ar)


    def checkImage2(self):
        return '''
            <!doctype html>
            <title>Upload new File</title>
            <h1>Проверка работы алгоритма</h1>
            <form method=post enctype=multipart/form-data>
              <input type=file name=file>
              <input type=submit value=Upload>
            </form>
            '''

