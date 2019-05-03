from seiya.db.job import session
from seiya.db.movie import Movie
from sqlalchemy.sql import func
from collections import Counter


def analysis_review_num():
    review_num_list = session.query(
            Movie.name, Movie.review_num).order_by(
            Movie.review_num.desc()).limit(10).all()
    data = [{'name':i[0], 'num': i[1]} for i in review_num_list]
    return data

def analysis_country():
    country_list = session.query(Movie.country).all()
    clean_country = []
    for i in country_list:
        for country in i[0].split():
            if '中国' in country:
                clean_country.append('中国大陆')
            else:
                clean_country.append(country)
    country_count = Counter(clean_country).most_common(10)
    data = [{'name': i[0], 'count': i[1]} for i in country_count]
    return data

def analysis_director():
    director_list = session.query(
            Movie.director, func.count(Movie.director)).group_by(
            Movie.director).order_by(func.count(
            Movie.director).desc()).limit(16).all()
    data = [{'name': i[0], 'count': i[1]} for i in director_list]
    return data

