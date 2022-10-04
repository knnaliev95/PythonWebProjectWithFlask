from admin.routes.imports import *

@admin_bp.route('/information', methods=['GET','POST'])
def information():
    informationform=OurInformationsForm()
    informations=OurInformations.query.all()
    return render_template('admin/information/information.html',informationform=informationform,informations=informations)

@admin_bp.route('/information/edit/<id>', methods=['GET','POST'])
def information_edit(id):
    from run import db
    informationform=OurInformationsForm()
    information=OurInformations.query.get(id)
    if request.method=='POST':
        information.location=informationform.location.data
        information.email=informationform.email.data
        information.phone=informationform.phone.data
        db.session.commit()
        return redirect('/admin/information')
    return render_template('admin/information/informationedit.html',informationform=informationform,information=information)