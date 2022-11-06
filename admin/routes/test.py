from admin.routes.imports import *

@admin_bp.route('/test', methods=['GET','POST'])
def test():
    testform=TestForm()
    department=Department.query.all()
    section=Section.query.all()
    return render_template('admin/test.html',testform=testform,department=department,section=section)