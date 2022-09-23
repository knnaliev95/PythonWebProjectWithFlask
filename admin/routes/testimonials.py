from admin.routes.imports import *

@admin_bp.route('/testimonials', methods=['GET','POST'])
def testimonials():
    testimonialsform=TestimonialsForm()
    testimonials=Testimanials.query.all()
    return render_template('admin/testimonials/testimonials.html',testimonialsform=testimonialsform,testimonials=testimonials)

@admin_bp.route('/testimonials/add', methods=['GET','POST'])
def testimonials_add():
    from run import db
    testimonialsform=TestimonialsForm()
    if request.method=='POST':
        file=request.files['image']
        filename=secure_filename(file.filename)
        extension=filename.rsplit('.',1)[1]
        new_filename=f'Testimonials{random.randint(1,2000)}.{extension}'
        file.save(os.path.join('./static/uploads/', new_filename))
        testimonial=Testimanials(
            name=testimonialsform.name.data,
            profession=testimonialsform.profession.data,
            image=new_filename,
            info=testimonialsform.info.data
        )
        db.session.add(testimonial)
        db.session.commit()
        return redirect('/admin/testimonials')

@admin_bp.route('/testimonials/delete/<id>', methods=['GET','POST'])
def testimonials_delete(id):
    from run import db
    testimonial=Testimanials.query.get(id)
    if request.method=='POST':
        filename=f"./static/uploads/{testimonial.image}"
        os.remove(filename)
        db.session.delete(testimonial)
        db.session.commit()
        return redirect('/admin/testimonials')

@admin_bp.route('/testimonials/edit/<id>', methods=['GET','POST'])
def testimonials_edit(id):
    from run import db
    testimonial=Testimanials.query.get(id)
    testimonialsform=TestimonialsForm()
    if request.method=='POST':
        if request.files['image']:
            file_name=f"./static/uploads/{testimonial.image}"
            os.remove(file_name)
            file=request.files['image']
            filename=secure_filename(file.filename)
            extension=filename.rsplit('.',1)[1]
            new_filename=f'Testimonials{random.randint(1,2000)}.{extension}'
            file.save(os.path.join('./static/uploads/', new_filename))
            testimonial.image=new_filename
        testimonial.name=testimonialsform.name.data
        testimonial.profession=testimonialsform.profession.data
        testimonial.info=testimonialsform.info.data
        db.session.commit()
        return redirect('/admin/testimonials')
    return render_template('admin/testimonials/testimonialsedit.html',testimonialsform=testimonialsform,testimonial=testimonial)