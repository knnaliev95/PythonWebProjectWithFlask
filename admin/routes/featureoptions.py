from admin.routes.imports import *

@admin_bp.route('/featureoptions', methods=['GET','POST'])
def featureoptions():
    from models import Features
    featureoptionsform=FeatureOptionsForm()
    featureoptions=FeatureOptions.query.all()
    features=Features.query.all()
    return render_template('admin/features/featureoptions.html',featureoptionsform=featureoptionsform,featureoptions=featureoptions,features=features,data=Features)

@admin_bp.route('/featureoptions/add', methods=['GET','POST'])
def featureoptions_add():
    from run import db
    featureoptionsform=FeatureOptionsForm()
    if request.method=='POST':
        featureoption=FeatureOptions(
            features_id=request.form['Featureoptions'],
            option=featureoptionsform.option.data
        )
        db.session.add(featureoption)
        db.session.commit()
        return redirect('/admin/featureoptions')

@admin_bp.route('/featureoptions/delete/<id>', methods=['GET','POST'])
def featureoptions_delete(id):
    from run import db
    featureoption=FeatureOptions.query.get(id)
    if request.method=='POST':
        db.session.delete(featureoption)
        db.session.commit()
        return redirect('/admin/featureoptions')

@admin_bp.route('/featureoptions/edit/<id>', methods=['GET','POST'])
def featureoptions_edit(id):
    from run import db
    featureoptionsform=FeatureOptionsForm()
    feature=Features.query.get(id)
    features=Features.query.all()
    if request.method=='POST':
        feature.features_id=request.form['Featureoptions']
        feature.option=featureoptionsform.option.data
        db.session.commit()
        return redirect('/admin/featureoptions')
    return render_template('admin/features/featureoptionsedit.html',featureoptionsform=featureoptionsform,feature=feature,features=features)