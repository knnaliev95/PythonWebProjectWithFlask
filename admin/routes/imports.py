from flask import render_template,redirect,request
from admin import admin_bp
from models import *
from admin.forms import *
import os
import random
from werkzeug.utils import secure_filename
from flask_login import login_required