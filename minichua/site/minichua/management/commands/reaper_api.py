from django.core.management.base import BaseCommand

import requests, json
from ...models import Mini

class Command(BaseCommand):

    def handle(self, *args, **options):
        r = requests.get('https://www.reapermini.com/api/productlist')
        json_data = json.loads(r.text)

        my_api = requests.get('http://localhost:8000/apis/v1')
        my_data = json.loads(my_api.text)
        # Mini.objects.all().delete()

        api = []
        categories = ['Warlord Army Packs', 'Warlord', 'Special Edition Figures', 'Savage Worlds', 'Reaper Dungeon Dwellers', 'Pathfinder Bones', 'Pathfinder', 'Numenara', 'Nefsokar', 'Necropolis', 'Mercenary', 'Holiday', 'Elves', 'Dwarves', 'Darkspawn', 'Dark Heaven Legends Army Packs', 'Dark Heaven Legends', 'Crusaders', 'Chronoscope Bones', 'Chronoscope', 'CAV: Strike Operations', 'Bones']
        count = 0
        checklist = []
        for obj in my_data:
            checklist.append(obj['name'])

        for item in json_data:
            if [ele for ele in categories if (ele in item['category'])]:
                if item['name'] not in checklist:
                    images = []
                    for img in item['images']:
                        images.append(img['URL'])
                    mini = Mini(
                        name = item['name'],
                        image_url = images,
                    )
                    mini.save()
                    count += 1
        print(f'done with {count} minis added')
        pass

##############   easier to read format #######################
# {"sku":"01404",
# "name":"2002 Christmas Sophie",
# "price":"15.99",
# "description":"",
# "images":[{"filename":"01404_G.jpg","type":"main","order":0,"artist":"","URL":"https://images.reapermini.com/4/01404_G.jpg"},{"filename":"01404_color.jpg","type":"painted","order":1,"artist":"Ed Pugh","URL":"https://images.reapermini.com/4/01404_color.jpg"}],
# "category":["Special Edition Figures"],
# "tags":["metal","female","demon","devil","christmas","bag of treats","succubus","chimney","presents"],
# "releaseDate":"1992-07-03T05:00:00.000Z",
# "weight":2.55,
# "material":"metal",
# "meta":{"assembly-required":true,"color":false,"painted":false},
# "barcode":{"withCheckDigit":"762486014048","withoutCheckDigit":"76248601404"}},
