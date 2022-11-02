import os
import random
import requests
import pprint
import re
from faker import Faker
from requests.auth import HTTPBasicAuth

pp = pprint.PrettyPrinter(indent=4)
fake = Faker("ru_RU")

adjectives = open("/code/adjectives.txt").readlines()
type_candys = open("/code/type.txt").readlines()
replacements=[(r'ый\b', 'ая'), (r'ой\b', 'ая'), (r'ий\b', 'ая')]



for i in range(10):
    adjective=random.choice(adjectives).rstrip().title()
    type_candy=random.choice(type_candys).rstrip().title()
    if (fake.boolean()):
        candy_name=adjective+' '+ fake.first_name_male()
    else:
        for pat,repl in replacements:
            adjective = re.sub(pat, repl, adjective)
            candy_name=adjective+' '+ fake.first_name_female()

    full_candy_info ={
        'name':candy_name,
        'company':fake.company(),
        'company_country':fake.country(),
        'company_address':fake.address(),
        'company_site':fake.url(),
        'company_email':fake.company_email(),
        'company_phone_number':fake.phone_number(),
        'company_director': fake.name(),
        'pricetag': re.sub(r'\xa0р\b', '₽', fake.pricetag()),
        'fats': fake.numerify(),
        'carbohydrates': fake.numerify(),
        'protein': fake.numerify(),
        'calories': fake.numerify(),
        'type': type_candy,
        'rating': fake.numerify()
    }

    r = requests.post('http://candydendy:8000/api',
                      auth=HTTPBasicAuth(
                          os.environ.get('TECH_NAME'),
                          os.environ.get('TECH_PASSWORD')
                      ),
                      json=full_candy_info)

    print(r.status_code)
