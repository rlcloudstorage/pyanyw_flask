""""""
from flask import (
    Blueprint, flash, g, redirect, render_template,
    request, session, url_for,
)


# bp = Blueprint('index', __name__, url_prefix='/')
bp = Blueprint('index', __name__)

@bp.route('/')
def index():
    return render_template('index.html')
