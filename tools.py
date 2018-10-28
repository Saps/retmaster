import random
from functools import wraps
from flask import session, request, redirect, url_for
from api.mainconfig import MCFG

def _get_random_string(length=12,
                      allowed_chars='abcdefghijklmnopqrstuvwxyz'
                                    'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    return ''.join(random.choice(allowed_chars) for i in range(length))


def get_secret_key():
    chars = 'sekrret'
    return _get_random_string(50, chars)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'sess_id' not in session:
            return redirect(url_for('resrc.loginWindow')) #, next=request.url))
        if not MCFG.checkSessionID(session['sess_id']):
            return redirect(url_for('resrc.loginWindow'))  # , next=request.url))
        return f(*args, **kwargs)
    return decorated_function

