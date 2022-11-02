from django.contrib.auth.models import User
from django.db import migrations
import os

def load_initial_data(apps, schema_editor):
    user = User.objects.create_user(
        os.environ.get('TECH_NAME'),
        os.environ.get('TECH_EMAIL'),
        os.environ.get('TECH_PASSWORD')
    )
    user.save()

class Migration(migrations.Migration):
    operations = [
       migrations.RunPython(load_initial_data)
    ]


