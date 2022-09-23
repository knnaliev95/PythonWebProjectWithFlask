from admin.routes.imports import *

@admin_bp.route('/featuredservice', methods=['GET','POST'])
def featuredservice():
    featuredserviceform=FeaturedserviceForm()
    featuredservices=FeaturedServices.query.all()
    return render_template('admin/featuredservice/featuredservice.html',featuredserviceform=featuredserviceform,featuredservices=featuredservices)

@admin_bp.route('/featuredservice/add', methods=['GET','POST'])
def featuredservice_add():
    featuredserviceform=FeaturedserviceForm()
    from run import db
    if request.method=='POST':
        featuredservice=FeaturedServices(
            icon=featuredserviceform.icon.data,
            name=featuredserviceform.name.data,
            info=featuredserviceform.info.data
        )
        db.session.add(featuredservice)
        db.session.commit()
        return redirect('/admin/featuredservice')

@admin_bp.route('/featuredservice/delete/<id>', methods=['GET','POST'])
def featuredservice_delete(id):
    from run import db
    featuredservice=FeaturedServices.query.get(id)
    if request.method=='POST':
        db.session.delete(featuredservice)
        db.session.commit()
        return redirect('/admin/featuredservice')

@admin_bp.route('/featuredservice/edit/<id>', methods=['GET','POST'])
def featuredservice_edit(id):
    from run import db
    service=FeaturedServices.query.get(id)
    featuredserviceform=FeaturedserviceForm()
    if request.method=='POST':
        service.icon=featuredserviceform.icon.data
        service.name=featuredserviceform.name.data
        service.info=featuredserviceform.info.data
        db.session.commit()
        return redirect('admin/featuredservice')
    return render_template('admin/feturedservice/featuredserviceedit.html',featuredserviceform=featuredserviceform,service=service)