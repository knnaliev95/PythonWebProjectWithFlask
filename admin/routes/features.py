from admin.routes.imports import *

@admin_bp.route('/features', methods=['GET','POST'])
def features():
    featuresform=FeaturesForm()
    features=Features.query.all()
    return render_template('admin/features/features.html',featuresform=featuresform,features=features)

@admin_bp.route('/features/add', methods=['GET','POST'])
def features_add():
    from run import db
    featuresform=FeaturesForm()
    if request.method=='POST':
        file=request.files['image']
        filename=secure_filename(file.filename)
        extension=filename.rsplit('.',1)[1]
        new_filename=f'Features{random.randint(1,2000)}.{extension}'
        file.save(os.path.join('./static/uploads/', new_filename))
        feature=Features(
            name=featuresform.name.data,
            icon=featuresform.icon.data,
            info=featuresform.info.data,
            image=new_filename,
            order=featuresform.order.data
        )
        db.session.add(feature)
        db.session.commit()
        return redirect('/admin/features')
    return render_template('admin/features/add',featuresform=featuresform)

@admin_bp.route('/features/delete/<id>', methods=['GET','POST'])
def features_delete(id):
    from run import db
    feature=Features.query.get(id)
    file_name=f"./static/uploads/{feature.image}"
    os.remove(file_name)
    db.session.delete(feature)
    db.session.commit()
    return redirect('/admin/features')

@admin_bp.route('/features/edit/<id>', methods=['GET','POST'])
def features_edit(id):
    featuresform=FeaturesForm()
    feature=Features.query.get(id)
    if request.method=='POST':
        if request.files['image']:
            file_name=f"./static/uploads/{feature.image}"
            os.remove(file_name)
            file=request.files['image']
            filename=secure_filename(file.filename)
            extension=filename.rsplit('.',1)[1]
            new_filename=f'Features{random.randint(1,2000)}.{extension}'
            file.save(os.path.join('./static/uploads/', new_filename))
            feature.image=new_filename
        feature.name=featuresform.name.data
        feature.icon=featuresform.icon.data
        feature.info=featuresform.info.data
        feature.order=featuresform.order.data
        db.session.commit()
        return redirect('/admin/features')
    return render_template('admin/features/featuresedit.html',featuresform=featuresform,feature=feature)