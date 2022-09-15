import random

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

from faker import Faker
from products.models import Product , Brand , Catergory



def seed_brand(n):
    fake = Faker()
    images =['1.jpg' , '2.png' , '3.jpg' , '4.png' , '5.jpg' ,'7.png' , '10.jpg']

    for _ in range(n):
        name = fake.name()
        image= f"Brand/{images[random.randint(0,4)]}"
       

        Brand.objects.create(
            name = name,
            image = image )



    print(f'Successfully seeded {n} brand')        

def seed_category(n):
    fake = Faker()
    images =['1.jpg' , '2.png' , '3.jpg' , '4.png' , '5.jpg','6.png','8.png']

    for _ in range(n):
        name = fake.name()
        image= f"Catergory/{images[random.randint(0,4)]}"
       

        Catergory.objects.create(
            name = name,
            image = image )
            
    print(f'Successfully seeded {n} category')        

def seed_products(n):
    fake = Faker()
    images =['1.jpg' , '2.png' , '3.jpg' , '4.png' , '5.jpg' ,'6.png' , '7.png' , '8.png' , '9.jpg' , '10.jpg']
    flag_type = ['New','Feature','Sale']
    for _ in range(n):
        name = fake.name()
        image= f"product/{images[random.randint(0,9)]}"
        sku= random.randint(1,100000)
        subtitle= fake.text(max_nb_chars=300)
        desc= fake.text(max_nb_chars=10000)
        flag= flag_type[random.randint(0,2)]
        price= round(random.uniform(20.99,99.99),2)
        category=Catergory.objects.get(id=random.randint(1,10))
        brand=Brand.objects.get(id=random.randint(1,10))



        Product.objects.create(
            name = name,
            image = image,
            sku=sku,
            subtitle=subtitle,
            desc=desc,
            flag=flag,
            price=price,
            video_url="https://www.youtube.com/watch?v=zVRgK9nF6yI"

            )
    print(f'Successfully seeded {n} product')        

#seed_brand(10)
#seed_category(10)
seed_products(1000)
