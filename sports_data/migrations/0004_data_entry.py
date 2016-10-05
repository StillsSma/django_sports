from __future__ import unicode_literals

from django.db import migrations, models
import csv


def add_sports_data(apps, schema_editor):
    Corn_husker = apps.get_model("sports_data","Corn_husker")
    with open('sports.csv') as f:
        reader = csv.reader(f)
        data = []
        for row in reader:
            for index, x in enumerate(row):
                if x == '':
                    row[index] = 0

            data.append(row)

        del data[0]

        for row in data:
            Corn_husker.objects.create(Player=row[0], Att=row[1],
            Yrds=row[2], Avg=row[3], TD=row[4])

class Migration(migrations.Migration):

    dependencies = [
        ('sports_data', '0003_corn_husker_player'),
    ]

    operations = [
    #    migrations.RunPython(add_sports_data)
    ]
