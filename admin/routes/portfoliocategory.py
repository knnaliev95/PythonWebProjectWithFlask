from admin.routes.imports import *

@admin_bp.route('/portfoliocategory', methods=['GET','POST'])
def portfoliocategory():
    portfoliocategoryform=PortfolioCategoryForm()
    categories=PortfolioCategory.query.all()
    return render_template('admin/portfolio/PortfolioCategory.html',portfoliocategoryform=portfoliocategoryform,categories=categories)

@admin_bp.route('/portfoliocategory/add', methods=['GET','POST'])
def portfoliocategory_add():
    from run import db
    from models import PortfolioCategory
    if request.method=='POST':
        category=PortfolioCategory(
            name=request.form['name']
        )
        db.session.add(category)
        db.session.commit()
        return redirect('/admin/portfoliocategory')

@admin_bp.route('/portfoliocategory/delete/<id>', methods=['GET','POST'])
def portfoliocategory_delete(id):
    from run import db
    portfoliocategory=PortfolioCategory.query.get(id)
    db.session.delete(portfoliocategory)
    db.session.commit()
    return redirect('/admin/portfoliocategory')

@admin_bp.route('/portfoliocategory/edit/<id>', methods=['GET','POST'])
def portfoliocategory_edit(id):
    from run import db
    category=PortfolioCategory.query.get(id)
    portfoliocategoryform=PortfolioCategoryForm()
    if request.method=='POST':
        category.name=portfoliocategoryform.name.data
        db.session.commit()
        return redirect('/admin/portfoliocategory')
    return render_template('admin/portfolio/portfoliocategoryedit.html',portfoliocategoryform=portfoliocategoryform,category=category)