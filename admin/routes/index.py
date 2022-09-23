from admin.routes.imports import *

@admin_bp.route('/', methods=['GET','POST'])
@login_required
def index():
    return render_template('admin/index.html')