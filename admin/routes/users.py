from admin.routes.imports import *

@admin_bp.route('/users', methods=['GET','POST'])
@login_required
def users():
    users=Users.query.all()[1:]
    return render_template('admin/users/index.html',users=users)

@admin_bp.route('/users/edit/<id>', methods=['GET','POST'])
@login_required
def users_edit(id):
    from run import db
    user=Users.query.get(id)
    if user.is_autorized:
        user.is_autorized=False
        db.session.commit()
    else:
        user.is_autorized=True
        db.session.commit()
    return redirect('/admin/users')

@admin_bp.route('/users/delete/<id>', methods=['GET','POST'])
@login_required
def users_delete(id):
    from run import db
    user=Users.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/admin/users')