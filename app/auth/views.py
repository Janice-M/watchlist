from flask import render_template,redirect,url_for,flash,request
from . import auth
from ..models import User
from .forms import RegistrationForm
from .. import db
from flask_login import login_user,logout_user,login_required
from ..models import User
from .forms import LoginForm,RegistrationForm
