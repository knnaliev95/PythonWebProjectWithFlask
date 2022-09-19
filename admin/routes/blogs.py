from admin.routes.imports import *

@admin_bp.route('/blog', methods=['GET','POST'])
def blog():
    blogform=BlogForm()
    blogs=Blogs.query.all()
    return render_template('admin/blog/blog.html',blogform=blogform,blogs=blogs)

@admin_bp.route('/blog/add', methods=['GET','POST'])
def blog_add():
    blogform=BlogForm()
    from run import db
    if request.method=='POST':
        file=request.files['image']
        filename=secure_filename(file.filename)
        extension=filename.rsplit('.',1)[1]
        new_filename=f'Blog{random.randint(1,2000)}.{extension}'
        file.save(os.path.join('./static/uploads/', new_filename))
        blog=Blogs(
            name=blogform.name.data,
            header=blogform.header.data,
            image=new_filename,
            content=blogform.content.data
        )
        db.session.add(blog)
        db.session.commit()
        return redirect('/admin/blog')

@admin_bp.route('/blog/delete/<id>',methods=['GET','POST'])
def blog_delete(id):
    from run import db
    blog=Blogs.query.get(id)
    file_name=f"./static/uploads/{blog.image}"
    os.remove(file_name)
    db.session.delete(blog)
    db.session.commit()
    return redirect('/admin/blog')

@admin_bp.route('/blog/edit/<id>', methods=['GET','POST'])
def blog_edit(id):
    from run import db
    blogform=BlogForm()
    blog=Blogs.query.get(id)
    if request.method=='POST':
        if request.files['image']:
            file_name=f"./static/uploads/{blog.image}"
            os.remove(file_name)
            file=request.files['image']
            filename=secure_filename(file.filename)
            extension=filename.rsplit('.',1)[1]
            new_filename=f'Blog{random.randint(1,2000)}.{extension}'
            file.save(os.path.join('./static/uploads/', new_filename))
            blog.image=new_filename
        blog.name=blogform.name.data
        blog.header=blogform.header.data
        blog.content=blogform.content.data
        db.session.commit()
        return redirect('/admin/blog')
    return render_template('admin/blog/blogedit.html',blogform=blogform,blog=blog)