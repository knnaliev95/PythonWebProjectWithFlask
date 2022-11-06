from flask import Blueprint,jsonify

api_bp=Blueprint('api',__name__,url_prefix='/api',static_folder='static',template_folder='templates',static_url_path='/api/static')

@api_bp.route('/departments')
def departments():
    from models import Department,DepartmentSchema
    department_schema=DepartmentSchema(many=True)
    departments=Department.query.all()
    output=department_schema.dump(departments)
    return jsonify(output)

@api_bp.route('/sections')
def sections():
    from models import Section,SectionSchema
    section_schema=SectionSchema(many=True)
    section=Section.query.all()
    output=section_schema.dump(section)
    return jsonify(output)