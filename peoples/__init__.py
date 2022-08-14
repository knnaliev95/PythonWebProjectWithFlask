from flask import Blueprint
peoples_bp=Blueprint('peoples',__name__,url_prefix='/',static_folder='static',template_folder='templates',static_url_path='/peoples/static')