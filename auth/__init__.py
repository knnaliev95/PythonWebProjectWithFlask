from flask import Blueprint

auth_bp=Blueprint('auth',__name__,url_prefix='/auth',static_folder='static',template_folder='templates',static_url_path='/auth/static')