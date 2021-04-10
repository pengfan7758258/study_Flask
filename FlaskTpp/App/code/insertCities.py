import json

import pymysql

mysql_args = {
    'user': 'pengfan758258',
    'password': "Pf@7758258",
    'host': 'rm-bp1nq96t1655pm4djmo.mysql.rds.aliyuncs.com',
    'database': 'FlaskTpp',
    'port': 3306,
    'charset': 'utf8'
}


def load_data():
    with open('cites.json', 'r', encoding='utf-8') as city_json:
        data = json.load(city_json)
    return data


def insert_cities(cities_json):
    cities = cities_json.get('returnValue')

    db = pymysql.connect(**mysql_args)  # 连接mysql数据库
    cursor = db.cursor()  # 创建游标

    keys = cities.keys()
    for key in keys:
        cursor.execute("insert into letter(letter) values ('%s')" % key)
        db.commit()
        letter_id = cursor.lastrowid

        cities_letter = cities.get(key)

        for city in cities_letter:
            c_id = city.get('id')
            c_parent_id = city.get('parentId')
            c_region_name = city.get('regionName')
            c_city_code = city.get('cityCode')
            c_pinyin = city.get('pinYin')
            cursor.execute(
                "insert into city(letter_id, c_id, c_parent_id, c_region_name, c_city_code, c_pinyin) values (%d,%d,%d,'%s',%d,'%s')" % (
                    letter_id, c_id, c_parent_id, c_region_name, c_city_code, c_pinyin))
            db.commit()
    db.close()


if __name__ == '__main__':
    cities_json = load_data()
    insert_cities(cities_json)
