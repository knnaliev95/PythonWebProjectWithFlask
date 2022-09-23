from admin.routes.imports import *

@admin_bp.route('/teamsimage', methods=['GET','POST'])
def teamsimage():
    from models import Teams
    teams=Teams.query.all()
    teamimagesform=TeamImagesForm()
    teamimages=TeamImages.query.all()
    return render_template('admin/teams/teamsimage.html',teams=teams,teamimagesform=teamimagesform,teamimages=teamimages,Teamsdata=Teams)

@admin_bp.route('/teamsimage/add', methods=['GET','POST'])
def teamsimage_add():
    from run import db
    if request.method=='POST':
        name=Teams.query.filter_by(Id=request.form['Teams']).first().Name
        files=request.files.getlist('image')
        for file in files:
            filename=secure_filename(file.filename)
            extension=filename.rsplit('.',1)[1]
            new_filename=f'TeamImages{random.randint(1,2000)}.{extension}'
            if os.path.isdir(f'./static/uploads/{name}'):
                file.save(os.path.join(f'./static/uploads/{name}/', new_filename))
            else:
                os.makedirs(f'./static/uploads/{name}')
                file.save(os.path.join(f'./static/uploads/{name}/', new_filename))
            teamsimage=TeamImages(
                Teamsid=request.form['Teams'],
                image=new_filename
            )
            db.session.add(teamsimage)
        db.session.commit()
        return redirect('/admin/teamsimage')

@admin_bp.route('/teamsimage/delete/<id>', methods=['GET','POST'])
def teamsimage_delete(id):
    from run import db
    image=TeamImages.query.get(id)
    if request.method=='POST':
        filename=f"./static/uploads/{image.image}"
        os.remove(filename)
        db.session.delete(image)
        db.session.commit()
        return redirect('/admin/teamsimage')