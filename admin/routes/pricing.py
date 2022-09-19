from admin.routes.imports import *

@admin_bp.route('/pricing', methods=['GET','POST'])
def pricing():
    pricingform=PricingForm()
    pricings=Pricing.query.all()
    return render_template('admin/pricing/pricing.html',pricingform=pricingform,pricings=pricings)

@admin_bp.route('/pricing/add', methods=['GET','POST'])
def pricing_add():
    from run import db
    pricingform=PricingForm()
    if request.method=='POST':
        price=Pricing(
            name=pricingform.name.data,
            amount=pricingform.amount.data
        )
        db.session.add(price)
        db.session.commit()
        return redirect('/admin/pricing')

@admin_bp.route('/pricing/delete/<id>', methods=['GET','POST'])
def pricing_delete(id):
    from run import db
    pricing=Pricing.query.get(id)
    db.session.delete(pricing)
    db.session.commit()
    return redirect('/admin/pricing')

@admin_bp.route('/pricing/edit/<id>', methods=['GET','POST'])
def pricing_edit(id):
    from run import db
    pricingform=PricingForm()
    pricing=Pricing.query.get(id)
    if request.method=='POST':
        pricing.name=pricingform.name.data
        pricing.amount=pricingform.amount.data
        db.session.commit()
        return redirect('/admin/pricing')
    return render_template('admin/pricing/pricingedit.html',pricingform=pricingform,pricing=pricing)