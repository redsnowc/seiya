from seiya.db.job import Job, session
from sqlalchemy.sql import func
from collections import Counter


def analysis_top10_city():
    city_list = session.query(
                Job.city, func.count(Job.city)).group_by(
                Job.city).order_by(func.count(Job.city).desc()).all()
    data = [{'name': i[0], 'amount': i[1]} for i in city_list][:10]
    return data


def analysis_top10_wage():
    salary_list = session.query(Job.city, func.avg(
            (Job.salary_upper+Job.salary_lower)/2)).group_by(
            Job.city).order_by(func.avg(
            (Job.salary_upper + Job.salary_lower) / 2).desc()).all()
    data = [{'name' : i[0], 'salary': float(i[1])}
            for i in salary_list][:10]
    return data

def analysis_tags():
    all_tags = session.query(Job.tags).all()
    tags_list = []
    for tags in all_tags:
        for tag in tags:
            tags_list += tag.split()
    tag_count = Counter(tags_list).most_common(10)
    '''
    tag_df = pd.DataFrame(tag_count).set_index(pd.DataFrame(
        tag_count)[0]).drop([0],axis=1)
     '''
    data = [{'tag': i[0], 'count': i[1]} for i in tag_count]
    return data

def analysis_experience():
    all_experience = session.query(Job.experience_lower, 
            Job.experience_upper).all()
    experience_count = Counter(all_experience).most_common()
    data = [{'experience': str(i[0][0]) + '-' + str(i[0][1]) + '年', 
             'count': i[1]} for i in experience_count]
    for i in data:
        if i['experience'] == '0-0年':
            i['experience'] = '不限'
    return data

def analysis_education():
    all_education = session.query(Job.education, 
            func.count(Job.education)).group_by(Job.education).all()
    total = sum([i[1] for i in all_education])
    data = [{'item': i[0], 'count': i[1], 
        'percent': round(i[1] / total, 2)} for i in all_education]
    return data

def analysis_cityedc_salary():
    all_cityedu_salary = session.query(Job.city, Job.education, 
            func.avg((Job.salary_upper + Job.salary_lower)/ 2)).group_by(
            Job.city, Job.education).all()
    data = [{'city': i[0], 'edc': i[1], 'salary': float(i[2])} 
            for i in all_cityedu_salary]
    return data

