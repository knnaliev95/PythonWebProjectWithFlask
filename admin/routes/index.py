from admin.routes.imports import *

@admin_bp.route('/', methods=['GET','POST'])
def index():
    return render_template('admin/index.html')