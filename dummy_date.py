import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()
from products.models import Brand,Category,product
from faker import Faker
import random
def seed_brand(n):
    fake =Faker()
    images= ['1.jpg','2.jpg','3.jpg','4.jpg','5.png',]
    
    for _ in range(n):
        name =fake.name()
        image =f"brand/{images[random.randint(0,4)]}"
        Brand.objects.create(
            name =name,
            image = image
        )
    print(f"Successfully Seeded{n} Branders")
def seed_category(n):
    fake =Faker()
    images= ['1.jpg','2.jpg','3.jpg','4.jpg','5.png','6.jpg','7.png']
    
    for _ in range(n):
        name =fake.name()
        image =f"Category/{images[random.randint(0,6)]}"
        Category.objects.create(
            name =name,
            image = image
        )
    print(f"Successfully Seeded{n} categorys")
def seed_product(n):
    fake =Faker()
    images= ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg']
    flags = ['New','Feature','sela']
    for _ in range(n):
        name =fake.name()
        sku = random.randint(1,100000)
        subtitle = fake.text(max_nb_chars=250)
        desc = fake.text(max_nb_chars=10000)
        flag = flags[random.randint(0,2)]
        price = round(random.uniform(20.99,999.99),2)
        image =f"products/{images[random.randint(0,9)]}"
        category =Category.objects.get(id=random.randint(1,57))
        brand =Brand.objects.get(id=random.randint(1,57))
        
        product.objects.create(
            name =name,
            image = image,
            sku = sku,
            subtitle = subtitle,
            desc = desc,
            flag = flag,
            price = price ,
            category = category,
            brand = brand,
            video_url='https://youtu.be/g4NvyfAEQn0'   
        )
    print(f"Successfully Seeded{n} products")

def new_func():
    return 60
#seed_brand(10)
#seed_category(20)
seed_product(1000000)
     