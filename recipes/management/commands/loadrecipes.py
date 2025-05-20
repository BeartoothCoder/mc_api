import json
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from recipes.models import Recipe

class Command(BaseCommand):
    help = "Load Minecraft crafting recipes from the `recipes_data/` directory (adjacent to `manage.py`)"

    def handle(self, *args, **kwargs):
        recipes_dir:Path = settings.BASE_DIR / 'recipes_data'
        if not recipes_dir.exists():
            raise CommandError('recipes_data directory does not exist')
        files = tuple(recipes_dir.glob('*.json'))
        if len(files) < 1:
            raise CommandError('recipes_data directory contains no .json files')
        if Recipe.objects.all().exists():
            confirm = input("Some recipe data already exists in the database. Wipe the database and proceed? [Y/n] ")
            if confirm.lower() != 'y':
                print('Abort.')
                exit()
        Recipe.objects.all().delete() # Wipe old records
        for filename in files:
            with open(filename, 'r') as f:
                data = json.load(f)
                json_str = json.dumps(data)
                if 'deprecated' not in json_str:
                    Recipe.objects.create(data=data)
        print('Done!')
        
        
        