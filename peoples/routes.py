from flask import Flask,render_template
from peoples import peoples_bp

@peoples_bp.route('/', methods=['GET','POST'])
def peoples_index():
    return render_template('peoples/index.html')