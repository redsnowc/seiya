from flask import Blueprint, render_template
from seiya.analysis.tenement import (analysis_top10_estate, analysis_unit,
        analysis_area, analysis_region, analysis_rent)


tenement_bp = Blueprint('tenement', __name__, url_prefix='/tenement')

@tenement_bp.route('/')
def index():
    return render_template('tenement/index.html')

@tenement_bp.route('/top10-estate')
def top10_estate():
    data = analysis_top10_estate()
    return render_template('tenement/top10_estate.html', estate_data=data)

@tenement_bp.route('/unit')
def unit():
    data = analysis_unit()
    return render_template('tenement/unit.html', unit_data=data)

@tenement_bp.route('/area')
def area():
    data = analysis_area()
    return render_template('tenement/area.html', area_data=data)

@tenement_bp.route('/region')
def region():
    data = analysis_region()
    return render_template('tenement/region.html', region_data=data)

@tenement_bp.route('/rent')
def rent():
    data = analysis_rent()
    return render_template('tenement/rent.html', rent_data=data)

