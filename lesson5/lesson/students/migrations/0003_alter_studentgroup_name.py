# Generated by Django 4.0.5 on 2022-06-25 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_studentgroup_student_birthday_alter_student_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentgroup',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя'),
        ),
    ]
