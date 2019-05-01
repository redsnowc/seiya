from seiya.db.job import session
from seiya.db.tenement import Tenement
from sqlalchemy.sql import func
from collections import Counter


def analysis_top10_estate():
    estate_list = session.query(
            Tenement.title, func.count(Tenement.title)).group_by(
            Tenement.title).order_by(
            func.count(Tenement.title).desc()).limit(11).all()
    for i in estate_list:
        if i[0] == '整租':
            estate_list.pop(estate_list.index(i))
    data = [{'name': i[0], 'amount': i[1]} for i in estate_list]
    return data 

def analysis_unit():
    unit_list = session.query(Tenement.unit, 
                func.count(Tenement.unit)).group_by(Tenement.unit).all()
    clean_unit = []
    count = 0
    for i in unit_list:
        if i[1] < 10:
            count += i[1]
        else: 
            clean_unit.append(i)
    clean_unit.append(('其他', count))
    total = sum([i[1] for i in clean_unit])
    data = [{'item': i[0], 'count': i[1], 
        'percent': round(i[1] / total, 2)} for i in clean_unit]
    return data

def analysis_area():
    area_list = session.query(Tenement.area, 
            func.count(Tenement.area)).group_by(Tenement.area).all()
    data = [{'area': i[0], 'count': i[1]} for i in area_list]
    return data

def analysis_region():
    region_list = session.query(Tenement.region, 
            func.count(Tenement.region)).group_by(
            Tenement.region).order_by(func.count(Tenement.region).desc()).all()
    data = [{'name': i[0], 'amount': i[1]} for i in region_list]
    return data

def analysis_rent():
    unit_list = session.query(Tenement.unit,
            func.count(Tenement.unit)).group_by(Tenement.unit).all()
    clean_unit = []
    for i in unit_list:
        if i[1] >= 10:
            clean_unit.append(i[0])
    data = []
    for unit in clean_unit:
        data += [{'unit': i[0], 'rent': i[1], 'name': i[2]} for i in 
                session.query(Tenement.unit, Tenement.rent, 
                Tenement.title).filter(Tenement.unit==unit, 
                Tenement.title!='整租').group_by(Tenement.unit, 
                Tenement.rent).order_by(Tenement.rent.desc()).limit(10).all()]
    return data

