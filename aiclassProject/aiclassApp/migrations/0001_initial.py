# Generated by Django 3.1.4 on 2020-12-16 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AiClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_num', models.IntegerField()),
                ('lecturer', models.CharField(max_length=30)),
                ('class_room', models.CharField(max_length=30)),
                ('students_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AiStudents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('class_num', models.IntegerField()),
                ('phone_num', models.CharField(max_length=30)),
                ('intro_text', models.TextField()),
            ],
        ),
    ]
