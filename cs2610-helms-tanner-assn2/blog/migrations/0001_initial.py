# Generated by Django 4.1.7 on 2023-02-22 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('posted', models.DateTimeField(verbose_name='Date Posted')),
                ('imageUrl', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commenter', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('content', models.TextField()),
                ('posted', models.DateTimeField(verbose_name='Date Posted')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
        ),
    ]
