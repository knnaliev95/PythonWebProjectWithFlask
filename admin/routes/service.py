from admin.routes.imports import *

@admin_bp.route('/service', methods=['GET','POST'])
def service():
    servicesform=ServiceForm()
    services=Services.query.all()
    return render_template('admin/service/service.html',servicesform=servicesform,services=services)

@admin_bp.route('/service/add', methods=['GET','POST'])
def service_add():
    from run import db
    serviceform=ServiceForm()
    if request.method=='POST':
        file=request.files['image']
        filename=secure_filename(file.filename)
        extension=filename.rsplit('.',1)[1]
        new_filename=f'Service{random.randint(1,2000)}.{extension}'
        file.save(os.path.join('./static/uploads/', new_filename))
        service=Services(
            name=serviceform.name.data,
            info=serviceform.info.data,
            icon=serviceform.icon.data,
            image=new_filename
        )
        db.session.add(service)
        db.session.commit()
        return redirect('/admin/service')

@admin_bp.route('/service/delete/<id>', methods=['GET','POST'])
def service_delete(id):
    from run import db
    service=Services.query.get(id)
    filename=f"./static/uploads/{service.image}"
    os.remove(filename)
    db.session.delete(service)
    db.session.commit()
    return redirect('/admin/service')

@admin_bp.route('/service/edit/<id>', methods=['GET','POST'])
def service_edit(id):
    from run import db
    servicesform=ServiceForm()
    service=Services.query.get(id)
    if request.method=='POST':
        if request.files['image']:
            file_name=f"./static/uploads/{service.image}"
            os.remove(file_name)
            file=request.files['image']
            filename=secure_filename(file.filename)
            extension=filename.rsplit('.',1)[1]
            new_filename=f'Service{random.randint(1,2000)}.{extension}'
            file.save(os.path.join('./static/uploads/', new_filename))
            service.image=new_filename
        service.name=servicesform.name.data
        service.info=servicesform.info.data
        service.icon=servicesform.icon.data
        db.session.commit()
        return redirect('/admin/service')
    return render_template('admin/service/serviceedit.html',servicesform=servicesform,service=service)