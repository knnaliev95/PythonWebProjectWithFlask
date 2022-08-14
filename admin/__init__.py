from flask import Blueprint

admin_bp=Blueprint('admin',__name__,url_prefix='/admin',static_folder='static',template_folder='templates',static_url_path='/admin/static')