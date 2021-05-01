from flask import Blueprint, render_template, request, jsonify

people_Aiden_bp = Blueprint('people_Aiden', __name__,
                              template_folder='aiden',
                              static_folder='static', static_url_path='assets')


@people_Aiden_bp.route('/aiden/')
def index():
    return render_template("randomcolorpicker.html")
