from admin.routes.imports import *

@admin_bp.route('/navlinks', methods=['GET','POST'])
def navlinks():
    navlinks=NavLinksForm()
    navigationlink=NavLinks.query.all()
    return render_template('admin/navbar/navlinks.html', navlinks=navlinks, navigationlink=navigationlink)

@admin_bp.route('/navlinks/add', methods=['GET','POST'])
def navlinks_add():
    from flask import session
    from run import db 
    navlinkForm=NavLinksForm()
    if request.method=='POST':
        navlink=NavLinks(
            Name=navlinkForm.name.data,
            Url=navlinkForm.url.data,
            Order=navlinkForm.order.data,
            IsActive=navlinkForm.isactive.data
        )
        db.session.add(navlink)
        db.session.commit()
        return redirect('/admin/navlinks')

@admin_bp.route('/navlinks/delete/<id>',methods=['GET','POST'])
def navlinks_delete(id):
    from run import db
    link=NavLinks.query.get(id)
    db.session.delete(link)
    db.session.commit()
    return redirect('/admin/navlinks')

@admin_bp.route('/navlinks/edit/<id>', methods=['GET','POST'])
def navlinks_edit(id):
    from run import db
    navlinks=NavLinks.query.get(id)
    navlinksform=NavLinksForm()
    if request.method=='POST':
        navlinks.Name=navlinksform.name.data
        navlinks.Url=navlinksform.url.data
        navlinks.Order=navlinksform.order.data
        navlinks.IsActive=navlinksform.isactive.data
        db.session.commit()
        return redirect('/admin/navlinks')
    return render_template('admin/navbar/navlinksedit.html',navlinksform=navlinksform,navlinks=navlinks)