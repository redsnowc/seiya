from flask import Blueprint, render_template
from seiya.analysis.movie import (analysis_review_num, analysis_country, 
        analysis_director)


movie_bp = Blueprint('movie', __name__, url_prefix='/movie')

@movie_bp.route('/')
def index():
    return render_template('movie/index.html')

@movie_bp.route('/review-num')
def review_num():
    data = analysis_review_num()
    return render_template('movie/review_num.html', review_data=data)

@movie_bp.route('/country')
def country():
    data = analysis_country()
    return render_template('movie/country.html', country_data=data)

@movie_bp.route('/director')
def director():
    data = analysis_director()
    return render_template('movie/director.html', director_data=data)

