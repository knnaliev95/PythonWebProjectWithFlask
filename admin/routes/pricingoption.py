from admin.routes.imports import *

@admin_bp.route('/pricingoption', methods=['GET','POST'])
def pricingoption():
    from models import Pricing
    pricings=Pricing.query.all()
    pricingoptionform=PricingOptionsForm()
    pricingoptions=PricingOptions.query.all()
    return render_template('admin/pricing/pricingoptions.html',pricings=pricings,pricingoptionform=pricingoptionform,pricingoptions=pricingoptions,Pricing=Pricing)

@admin_bp.route('/pricingoption/add', methods=['GET','POST'])
def pricingoption_add():
    from run import db
    pricingoptionform=PricingOptionsForm()
    if request.method=='POST':
        pricingoption=PricingOptions(
            pricing_id=request.form['pricing'],
            option=pricingoptionform.option.data
        )
        db.session.add(pricingoption)
        db.session.commit()
        return redirect('/admin/pricingoption')

@admin_bp.route('/pricingoption/delete/<id>', methods=['GET','POST'])
def pricingoption_delete(id):
    from run import db
    pricingoption=PricingOptions.query.get(id)
    db.session.delete(pricingoption)
    db.session.commit()
    return redirect('/admin/pricingoption')

@admin_bp.route('/pricingoption/edit/<id>', methods=['GET','POST'])
def procongoptions_edit(id):
    from run import db
    pricingoptionform=PricingOptionsForm()
    pricingoption=PricingOptions.query.get(id)
    pricings=Pricing.query.all()
    if request.method=='POST':
        pricingoption.pricing_id=request.form['pricing']
        pricingoption.option=pricingoptionform.option.data
        db.session.commit()
        return redirect('/admin/pricingoption')
    return render_template('admin/pricing/pricingoptionsedit.html',pricingoptionform=pricingoptionform,pricingoption=pricingoption,pricings=pricings)