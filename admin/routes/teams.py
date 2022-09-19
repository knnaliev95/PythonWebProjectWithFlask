from admin.routes.imports import *

@admin_bp.route('/teams', methods=['GET','POST'])
def teams():
    teamsform=TeamsForm()
    teams=Teams.query.all()
    return render_template('admin/teams/teams.html', teamsform=teamsform, teams=teams)

@admin_bp.route('/teams/add', methods=['GET','POST'])
def teams_add():
    from run import db
    teamsform=TeamsForm()
    if request.method=='POST':
        file=request.files['image']
        filename=secure_filename(file.filename)
        extension=filename.rsplit('.',1)[1]
        new_filename=f'Teams{random.randint(1,2000)}.{extension}'
        file.save(os.path.join('./static/uploads/', new_filename))
        team=Teams(
            Name=teamsform.name.data,
            Profession=teamsform.profession.data,
            Image=new_filename,
            TwitterAdress=teamsform.twitter.data,
            FacebookAdress=teamsform.facebook.data,
            InstagramAdress=teamsform.instagram.data,
            LinkedinAdress=teamsform.linkedin.data,
            Order=teamsform.order.data,
            IsActive=teamsform.isactive.data
        )
        db.session.add(team)
        db.session.commit()
        return redirect('/admin/teams')

@admin_bp.route('/teams/delete/<id>')
def teams_delete(id):
    from run import db
    team=Teams.query.get(id)
    filename=f"./static/uploads/{team.Image}"
    os.remove(filename)
    db.session.delete(team)
    db.session.commit()
    return redirect('/admin/teams')

@admin_bp.route('/teams/edit/<id>', methods=['GET','POST'])
def teams_edit(id):
    from run import db
    team=Teams.query.get(id)
    teamsform=TeamsForm()
    if request.method=='POST':
        if request.files['image']:
            file_name=f"./static/uploads/{team.Image}"
            os.remove(file_name)
            file=request.files['image']
            filename=secure_filename(file.filename)
            extension=filename.rsplit('.',1)[1]
            new_filename=f'Teams{random.randint(1,2000)}.{extension}'
            file.save(os.path.join('./static/uploads/', new_filename))
            team.Image=new_filename
        team.Name=teamsform.name.data
        team.Profession=teamsform.profession.data
        team.TwitterAdress=teamsform.twitter.data
        team.FacebookAdress=teamsform.facebook.data
        team.InstagramAdress=teamsform.instagram.data
        team.LinkedinAdress=teamsform.linkedin.data
        team.Order=teamsform.order.data
        team.IsActive=teamsform.isactive.data
        db.session.commit()
    return render_template('admin/teams/teamsedit.html',team=team, teamsform=teamsform)