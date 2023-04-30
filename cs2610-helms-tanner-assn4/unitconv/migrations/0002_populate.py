from django.db import migrations

from unitconv.models import Convert


def create_conversions(apps, schema_editor):
    T = Convert()
    T.Name = "T"
    T.Factor = 29166.7
    T.save()

    g = Convert()
    g.Name = "g"
    g.Factor = 0.0321507
    g.save()

    t_oz = Convert()
    t_oz.Name = "t_oz"
    t_oz.Factor = 1
    t_oz.save()

    kg = Convert()
    kg.Name = "kg"
    kg.Factor = 32.1507
    kg.save()

    lb = Convert()
    lb.Name = "lb"
    lb.Factor = 14.5833
    lb.save()

    oz = Convert()
    oz.Name = "oz"
    oz.Factor = 0.911458
    oz.save()


class Migration(migrations.Migration):
    dependencies = [
        ('unitconv', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_conversions)
    ]
