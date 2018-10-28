# -*- coding: utf-8 -*-
from flask import Blueprint
from .main import MainResource
from tools import login_required
from flask import request

resrc = Blueprint('resrc', __name__,
                  template_folder='templates')

# declaring default resources
p = MainResource()

@resrc.route('/')
def defaultPage():
    return p.defaultPage()


@resrc.route('/login', methods=['GET', 'POST'])
def loginWindow():
    return p.loginWindow()


@resrc.route('/logout')
def logoutWindow():
    return p.logoutWindow()


@resrc.route('/main')
def mainWindow():
    return p.mainPage()

@resrc.route('/check',methods=['GET', 'POST'])
def checkImage():
    if request.method == 'POST':
        return p.checkImage()
    else:
        return p.checkImage2()


@resrc.route('/<path:command>', methods=['GET', 'POST'])
def routeCall(command):
    pass #return p.routeCall(command)