import csv
import json


def change_dictionary(dictionary: dict) -> dict:
    for key, value in dictionary.items():
        if value.isdigit():
            dictionary[key] = int(value)
        elif value.lower() in ('true', 'false'):
            dictionary[key] = True if value.lower() == 'true' else False
    return dictionary


def get_fixture(dictionary: dict, name_model) -> dict:
    fields = {}
    pk = dictionary.pop('id')

    for key, value in dictionary.items():
        if key != 'location_id':
            fields[key] = value

    fixture = {'model': name_model,
               'pk': pk,
               'fields': fields}
    return fixture


def csv_to_json(file_csv: str, file_json: str, fieldnames: list, name_model: str) -> None:
    with open(file_csv, encoding='UTF-8') as csv_file:
        csv_reader = csv.DictReader(csv_file, fieldnames=fieldnames)
        data = map(lambda i: change_dictionary(i), csv_reader)
        data = list(map(lambda i: get_fixture(i, name_model), data))
        data.pop(0)

    with open(file_json, 'w', encoding='UTF-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)


fieldnames = ['id', 'name', 'author_id', 'price', 'description', 'is_published', 'image', 'category_id']
csv_to_json('ad.csv', 'ad.json', fieldnames, 'ads.ad')

fieldnames = ['id', 'name']
csv_to_json('category.csv', 'category.json', fieldnames, 'ads.category')

fieldnames = ['id', 'name', 'lat', 'lng']
csv_to_json('location.csv', 'location.json', fieldnames, 'users.location')

fieldnames = ['id', 'first_name', 'last_name', 'username', 'password', 'role', 'age', 'location_id']
csv_to_json('user.csv', 'user.json', fieldnames, 'users.user')

