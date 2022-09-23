from admin.routes.imports import *

@admin_bp.route('/clients', methods=['GET','POST'])
def clients():
    clientform=ClientsForm()
    clients=Clients.query.all()
    return render_template('admin/clients/clients.html', clientform=clientform,clients=clients)

@admin_bp.route('/clients/add', methods=['GET','POST'])
def clients_add():
    from run import db
    if request.method=='POST':
        file=request.files['image']
        filename=secure_filename(file.filename)
        extension=filename.rsplit('.',1)[1]
        new_filename=f'Clients{random.randint(1,2000)}.{extension}'
        file.save(os.path.join('./static/uploads/', new_filename))
        client=Clients(
            image=new_filename
        )
        db.session.add(client)
        db.session.commit()
        return redirect('/admin/clients')

@admin_bp.route('/clients/delete/<id>', methods=['GET','POST'])
def clients_delete(id):
    from run import db
    client=Clients.query.get(id)
    if request.method=='POST':
        filename=f"./static/uploads/{client.image}"
        os.remove(filename)
        db.session.delete(client)
        db.session.commit()
        return redirect('/admin/clients')