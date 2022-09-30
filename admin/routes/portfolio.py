from admin.routes.imports import *

@admin_bp.route('/portfolio', methods=['GET','POST'])
def portfolio():
    from models import PortfolioCategory
    categoies=PortfolioCategory.query.all()
    portfolios=Portfolio.query.all()
    portfolioform=PortfolioForm()
    return render_template('admin/portfolio/portfolio.html',portfolioform=portfolioform,categoies=categoies,portfolios=portfolios,PortfolioCategory=PortfolioCategory)

@admin_bp.route('/portfolio/add', methods=['GET','POST'])
def protfolio_add():
    from run import db
    from models import Portfolio
    portfolioform=PortfolioForm()
    if request.method=='POST':
        file=request.files['img']
        filename=secure_filename(file.filename)
        extension=filename.rsplit('.',1)[1]
        new_filename=f'Portfolio{random.randint(1,2000)}.{extension}'
        file.save(os.path.join('./static/uploads/', new_filename))
        portfolio=Portfolio(
            name=portfolioform.name.data,
            Category_id=request.form['Category'],
            img=new_filename,
            info=portfolioform.info.data
        )
        db.session.add(portfolio)
        db.session.commit()
        return redirect('/admin/portfolio')

@admin_bp.route('/portfolio/delete/<id>', methods=['GET','POST'])
def portfolio_delete(id):
    from run import db
    portfolio=Portfolio.query.get(id)
    filename=f"./static/uploads/{portfolio.img}"
    os.remove(filename)
    db.session.delete(portfolio)
    db.session.commit()
    return redirect('/admin/portfolio')

@admin_bp.route('/portfolio/edit/<id>', methods=['GET','POST'])
def portfolio_edit(id):
    from run import db
    portfolioform=PortfolioForm()
    categories=PortfolioCategory.query.all()
    portfolio=Portfolio.query.get(id)
    if request.method=='POST':
        if request.files['img']:
            file_name=f"./static/uploads/{portfolio.img}"
            os.remove(file_name)
            file=request.files['img']
            filename=secure_filename(file.filename)
            extension=filename.rsplit('.',1)[1]
            new_filename=f'Portfolio{random.randint(1,2000)}.{extension}'
            file.save(os.path.join('./static/uploads/', new_filename))
            portfolio.img=new_filename
        portfolio.name=portfolioform.name.data
        portfolio.Category_id=request.form['Category']
        portfolio.info=portfolioform.info.data
        db.session.commit()
        return redirect('/admin/portfolio')
    return render_template('admin/portfolio/portfolioedit.html',portfolioform=portfolioform,portfolio=portfolio,categories=categories)