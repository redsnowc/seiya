from flask import Blueprint, render_template, jsonify
from seiya.analysis.job import (analysis_top10_city, analysis_top10_wage,
        analysis_tags, analysis_experience, analysis_education,
        analysis_cityedc_salary)


job_bp = Blueprint('job', __name__, url_prefix='/job')

@job_bp.route('/')
def index():
    return render_template('job/index.html')

@job_bp.route('/top10-city')
def top10_city():
    data = analysis_top10_city()
    return render_template('job/top10_city.html', city_data=data)

@job_bp.route('/top10-wage')
def top10_wage():
    data = analysis_top10_wage()
    return render_template('job/top10_wage.html', salary_data=data)

@job_bp.route('/top10-tag')
def top10_tag():
    data = analysis_tags()
    return render_template('job/top10_tag.html', tag_data=data)

@job_bp.route('/experience')
def experience():
    data = analysis_experience()
    return render_template('job/experience.html', experience_data=data)

@job_bp.route('/education')
def education():
    data = analysis_education()
    return render_template('job/education.html', education_data=data)

@job_bp.route('/city-edu-salary')
def cityedu_salary():
    data = analysis_cityedc_salary()
    print(data)
    return render_template('job/cityedu_salary.html', ces_data=data)

